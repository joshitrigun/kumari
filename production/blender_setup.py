"""
blender_setup.py — The King's Regret
Full shot-by-shot Blender scene scaffold.

Run in Blender: Scripting workspace → Open file → Alt+P

Creates:
  • Scene settings (1920×1080, 24fps, 7200 frames)
  • 17 shot Collections, each with:
      - Grease Pencil object (character + FX layers pre-named)
      - Camera object (positioned for shot type)
      - Timeline markers (shot start/end)
  • 4 act lighting rigs
  • Color swatch materials (all palette colors)
  • Custom properties for shot navigation
"""

import bpy
import bmesh
import math
from mathutils import Vector, Euler

# ─────────────────────────────────────────────────────────────────────────────
# SHOT DATA
# Each entry: (num, label, start_frame, end_frame, act, characters, cam_type)
#
# characters: which layers to create on the GP object
#   "King"  "Taleju"  "Queen"  "Child"
# cam_type: positioning hint
#   wide | dolly | medium | close | pullback | track | static | extreme | rise | push_in
# ─────────────────────────────────────────────────────────────────────────────
SHOTS = [
    ( 1, "FadeIn_Establish",      1,    120, 1, ["King", "Taleju"],               "wide"),
    ( 2, "Dolly_Table",         121,    360, 1, ["King", "Taleju"],               "dolly"),
    ( 3, "Hands_Token",         361,    720, 1, ["King", "Taleju"],               "medium"),
    ( 4, "TwoShot",             721,   1200, 1, ["King", "Taleju", "Queen"],      "medium"),
    ( 5, "EyesMeeting_PEAK",   1201,   1752, 1, ["King", "Taleju"],               "close"),
    ( 6, "LightingShift",      1753,   2400, 2, ["King"],                         "close"),
    ( 7, "HeReaches",          2401,   2712, 2, ["King", "Taleju"],               "medium"),
    ( 8, "Vanishing_Token",    2713,   3336, 2, ["King", "Taleju"],               "pullback"),
    ( 9, "Flashback_Smile",    3337,   3840, 1, ["Taleju"],                       "close"),
    (10, "Rain_Walk",          3841,   4320, 3, ["King"],                         "track"),
    (11, "Dream_Vision",       4321,   4680, 3, ["King", "Taleju"],               "static"),
    (12, "Meditation",         4681,   5016, 3, ["King"],                         "static"),
    (13, "Montage",            5017,   5712, 3, ["King"],                         "extreme"),
    (14, "Dream_Peak",         5713,   6024, 3, ["King", "Taleju"],               "rise"),
    (15, "Kumari_Appears_PEAK",6025,   6720, 4, ["King", "Child"],                "track"),
    (16, "People_Bow",         6721,   7080, 4, ["King", "Child"],                "wide"),
    (17, "Epilogue_Token",     7081,   7200, 4, ["King"],                         "push_in"),
]

ACT_FRAME_RANGES = {
    1: (1,    1752),
    2: (1753, 3840),
    3: (3841, 6024),
    4: (6025, 7200),
}

# Camera (x, y, z, rx_deg, rz_deg) per cam_type
# Coordinate system: X=right, Y=depth, Z=up. Camera looks along -Y by default.
CAMERA_PRESETS = {
    "wide":      ( 0.0, -12.0, 5.0,  68, 0),   # Far wide establish
    "dolly":     ( 0.0,  -9.0, 4.0,  70, 0),   # Moderate push-in start
    "medium":    ( 0.2,  -6.5, 3.0,  72, 0),   # Two-shot distance
    "close":     ( 0.0,  -4.0, 2.5,  75, 0),   # Face/hands focus
    "pullback":  ( 0.0,  -5.0, 3.0,  72, 0),   # Starts medium, pulls
    "track":     (-3.0,  -6.0, 2.8,  74, 15),  # Side angle, tracks left→right
    "static":    ( 0.5,  -5.5, 2.5,  75, -5),  # Slightly off-axis, locked
    "extreme":   ( 0.0,  -2.5, 1.8,  80, 0),   # Extreme close-up (eyes/hands)
    "rise":      ( 0.0,  -6.0, 2.5,  72, 0),   # Starts medium, rises up
    "push_in":   ( 0.0,  -5.0, 3.0,  72, 0),   # Slow push toward subject
}

# Grease Pencil layer colours (R, G, B) for visual distinction in Blender
LAYER_COLORS = {
    "BG_Sky":          (0.30, 0.55, 0.90),
    "BG_Architecture": (0.55, 0.38, 0.22),
    "BG_Props":        (0.75, 0.52, 0.20),
    "FX_Smoke":        (0.72, 0.72, 0.72),
    "FX_Light":        (1.00, 0.90, 0.30),
    "FX_Rain":         (0.50, 0.68, 0.85),
    "CHAR_King":       (0.75, 0.18, 0.18),
    "CHAR_Taleju":     (0.95, 0.82, 0.20),
    "CHAR_Queen":      (0.60, 0.25, 0.65),
    "CHAR_Child":      (0.95, 0.55, 0.30),
}

ACT_MARKER_COLORS = {
    1: (0.90, 0.75, 0.15),  # Gold
    2: (0.30, 0.50, 0.80),  # Blue
    3: (0.38, 0.48, 0.55),  # Grey-blue
    4: (0.85, 0.60, 0.25),  # Dawn orange
}

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def get_or_create_collection(name, parent=None):
    if name in bpy.data.collections:
        col = bpy.data.collections[name]
    else:
        col = bpy.data.collections.new(name)
        target = parent if parent else bpy.context.scene.collection
        target.children.link(col)
    return col


def layers_for_shot(shot_num, act, characters):
    """Return ordered layer list for this shot."""
    layers = ["BG_Sky", "BG_Architecture", "BG_Props"]
    if act == 3:
        layers.append("FX_Rain")
    layers.append("FX_Smoke")
    for char in ["King", "Taleju", "Queen", "Child"]:
        if char in characters:
            layers.append(f"CHAR_{char}")
    layers.append("FX_Light")
    return layers


# ─────────────────────────────────────────────────────────────────────────────
# 1. BASE SCENE
# ─────────────────────────────────────────────────────────────────────────────

def setup_scene():
    if "Cube" in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects["Cube"], do_unlink=True)

    scene = bpy.context.scene
    scene.render.fps = 24
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    scene.frame_start = 1
    scene.frame_end = 7200
    scene.frame_current = 1

    # World: black background
    world = scene.world
    if world is None:
        world = bpy.data.worlds.new("World")
        scene.world = world
    try:
        world.use_nodes = True
        bg = world.node_tree.nodes.get("Background")
        if bg:
            bg.inputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
            bg.inputs[1].default_value = 0.0
    except Exception:
        pass

    # Custom prop: which shot is active (for reference)
    scene["kings_regret_active_shot"] = 1
    scene["kings_regret_total_shots"] = 17

    print("✓ Scene: 1920×1080 @ 24fps, 7200 frames (5:00)")


# ─────────────────────────────────────────────────────────────────────────────
# 2. TIMELINE MARKERS — all 17 shots + 4 act boundaries
# ─────────────────────────────────────────────────────────────────────────────

def setup_timeline_markers():
    scene = bpy.context.scene
    scene.timeline_markers.clear()

    # Act boundary markers
    act_events = [
        (1,    "ACT1_Start",        ACT_MARKER_COLORS[1]),
        (1753, "ACT2_Transgression",ACT_MARKER_COLORS[2]),
        (2713, "VANISHING_1:53",    ACT_MARKER_COLORS[2]),
        (3841, "ACT3_Penance",      ACT_MARKER_COLORS[3]),
        (4320, "DREAM_3:00",        ACT_MARKER_COLORS[3]),
        (6025, "ACT4_Rebirth",      ACT_MARKER_COLORS[4]),
        (7200, "END_5:00",          (0.7, 0.7, 0.7)),
    ]
    for frame, name, color in act_events:
        m = scene.timeline_markers.new(name)
        m.frame = frame
        try: m.color = color
        except AttributeError: pass

    # Per-shot start markers
    for num, label, start, end, act, chars, cam in SHOTS:
        name = f"S{num:02d}_{label}"
        m = scene.timeline_markers.new(name)
        m.frame = start
        try: m.color = ACT_MARKER_COLORS[act]
        except AttributeError: pass

    print(f"✓ Timeline: {len(act_events)} act markers + {len(SHOTS)} shot markers")


# ─────────────────────────────────────────────────────────────────────────────
# 3. COLLECTIONS — nested by act → shot
# ─────────────────────────────────────────────────────────────────────────────

def setup_collections():
    root = get_or_create_collection("KingsRegret")

    act_names = {
        1: "Act1_GoldenEra",
        2: "Act2_Transgression",
        3: "Act3_Penance",
        4: "Act4_Rebirth",
    }
    act_cols = {act: get_or_create_collection(name, root)
                for act, name in act_names.items()}

    shot_cols = {}
    for num, label, start, end, act, chars, cam in SHOTS:
        col_name = f"Shot_{num:02d}_{label}"
        col = get_or_create_collection(col_name, act_cols[act])
        shot_cols[num] = col

    # Shared collections
    get_or_create_collection("Cameras", root)
    get_or_create_collection("Lights", root)
    get_or_create_collection("Reference", root)

    print(f"✓ Collections: 4 acts, {len(SHOTS)} shot folders")
    return shot_cols


# ─────────────────────────────────────────────────────────────────────────────
# 4. GREASE PENCIL — one GP object per shot with named layers
# ─────────────────────────────────────────────────────────────────────────────

def create_grease_pencil_object(shot_num, label, start_frame, act, characters, collection):
    """Create a Grease Pencil object with pre-named layers for one shot."""
    gp_name = f"GP_S{shot_num:02d}_{label}"

    # Remove existing if re-running
    if gp_name in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects[gp_name], do_unlink=True)
    if gp_name in bpy.data.grease_pencils:
        bpy.data.grease_pencils.remove(bpy.data.grease_pencils[gp_name])

    gpd = bpy.data.grease_pencils.new(gp_name)
    gp_obj = bpy.data.objects.new(gp_name, gpd)
    collection.objects.link(gp_obj)

    # Stroke color mode
    gpd.stroke_depth_order = '2D'

    layer_list = layers_for_shot(shot_num, act, characters)

    for layer_name in reversed(layer_list):  # reversed = bottom layer first in stack
        layer = gpd.layers.new(layer_name)
        color = LAYER_COLORS.get(layer_name, (0.5, 0.5, 0.5))
        try: layer.tint_color = color
        except Exception: pass

        # Hide non-character layers by default (keeps viewport clean)
        if layer_name.startswith("BG_") or layer_name.startswith("FX_"):
            layer.hide = False
            layer.lock = False
        else:
            layer.hide = False
            layer.lock = False

        # Create a blank keyframe at this shot's start frame
        layer.frames.new(start_frame)

    # Set active layer to first character layer
    char_layer_name = f"CHAR_{characters[0]}" if characters else layer_list[-1]
    for layer in gpd.layers:
        if layer.name == char_layer_name:
            gpd.layers.active = layer
            break

    # Custom property: which shot this belongs to
    gp_obj["shot_number"] = shot_num
    gp_obj["shot_label"] = label
    gp_obj["shot_start"] = start_frame

    return gp_obj


def setup_all_grease_pencil(shot_cols):
    for num, label, start, end, act, chars, cam in SHOTS:
        col = shot_cols[num]
        create_grease_pencil_object(num, label, start, act, chars, col)
    print(f"✓ Grease Pencil: {len(SHOTS)} GP objects with named layers")


# ─────────────────────────────────────────────────────────────────────────────
# 5. CAMERAS — one per shot, positioned by cam_type
# ─────────────────────────────────────────────────────────────────────────────

def create_shot_camera(shot_num, label, cam_type, collection):
    cam_name = f"Cam_S{shot_num:02d}_{label}"

    if cam_name in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects[cam_name], do_unlink=True)
    if cam_name in bpy.data.cameras:
        bpy.data.cameras.remove(bpy.data.cameras[cam_name])

    cam_data = bpy.data.cameras.new(cam_name)
    cam_data.lens = 50
    cam_data.sensor_width = 36
    cam_data.dof.use_dof = False

    # Tighter lens for close shots
    if cam_type in ("close", "extreme"):
        cam_data.lens = 85
    elif cam_type in ("wide",):
        cam_data.lens = 35

    cam_obj = bpy.data.objects.new(cam_name, cam_data)
    collection.objects.link(cam_obj)

    x, y, z, rx, rz = CAMERA_PRESETS.get(cam_type, CAMERA_PRESETS["medium"])
    cam_obj.location = Vector((x, y, z))
    cam_obj.rotation_euler = Euler((
        math.radians(rx),
        0.0,
        math.radians(rz)
    ), 'XYZ')

    cam_obj["shot_number"] = shot_num
    cam_obj["cam_type"] = cam_type
    return cam_obj


def setup_all_cameras(shot_cols):
    cam_col = bpy.data.collections.get("Cameras")
    if cam_col is None:
        cam_col = bpy.data.collections.new("Cameras")
        bpy.context.scene.collection.children.link(cam_col)

    # Default/master camera (used for playback)
    master_cam_data = bpy.data.cameras.new("Camera_Master")
    master_cam_data.lens = 50
    master_cam = bpy.data.objects.new("Camera_Master", master_cam_data)
    cam_col.objects.link(master_cam)
    master_cam.location = Vector((0.0, -8.0, 3.5))
    master_cam.rotation_euler = Euler((math.radians(68), 0, 0))
    bpy.context.scene.camera = master_cam

    # Per-shot cameras
    for num, label, start, end, act, chars, cam_type in SHOTS:
        col = shot_cols[num]
        create_shot_camera(num, label, cam_type, col)

    print(f"✓ Cameras: 1 master + {len(SHOTS)} shot cameras")


# ─────────────────────────────────────────────────────────────────────────────
# 6. LIGHTING RIGS
# ─────────────────────────────────────────────────────────────────────────────

def create_light(name, light_type, energy, color, location, rotation_deg=(0, 0, 0), collection=None):
    if name in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects[name], do_unlink=True)
    light_data = bpy.data.lights.new(name, type=light_type)
    light_data.energy = energy
    light_data.color = color
    obj = bpy.data.objects.new(name, light_data)
    target = collection if collection else bpy.context.scene.collection
    target.objects.link(obj)
    obj.location = Vector(location)
    obj.rotation_euler = Euler([math.radians(d) for d in rotation_deg])
    return obj


def setup_lighting():
    light_col = bpy.data.collections.get("Lights")

    # ── ACT 1: Warm candlelight ──────────────────────────────────────────────
    create_light("L1_Key",  "SUN",   1500, (1.00, 0.90, 0.50),  ( 5, -5, 4), (45, 0, 45),  light_col)
    create_light("L1_Fill", "SUN",    600, (0.95, 0.85, 0.70),  (-3,  3, 3), (60, 0,-60),  light_col)
    create_light("L1_Rim",  "POINT",  500, (1.00, 0.80, 0.30),  (-6,  0, 2), (0, 0, 0),    light_col)

    # ── ACT 2: Cool harsh side-key ───────────────────────────────────────────
    create_light("L2_Key",  "SUN",   1000, (0.60, 0.80, 1.00),  ( 8, -2, 3), (70, 0, 30),  light_col)
    create_light("L2_Fill", "SUN",    200, (0.70, 0.80, 0.90),  (-1,  1, 1), (80, 0,-20),  light_col)

    # ── ACT 3: Near dark, one warm lamp ──────────────────────────────────────
    create_light("L3_Lamp",    "POINT",  800, (1.00, 0.70, 0.30),  (2, 2, 1.5), (0, 0, 0),   light_col)
    create_light("L3_Ambient", "SUN",    100, (0.50, 0.60, 0.70),  (0, 0, 5),   (90, 0, 0),  light_col)

    # ── ACT 4: Low sunrise ───────────────────────────────────────────────────
    create_light("L4_Key",  "SUN",   1200, (1.00, 0.85, 0.60),  ( 6, -6, 1.5), (80, 0, 45), light_col)
    create_light("L4_Fill", "SUN",    700, (0.85, 0.75, 0.95),  (-3,  3, 3),   (60, 0,-45), light_col)

    # All lights default to hidden — animator enables the relevant act's lights
    for obj in light_col.objects:
        obj.hide_viewport = True
        obj.hide_render = True

    # Un-hide Act 1 to start
    for name in ("L1_Key", "L1_Fill", "L1_Rim"):
        if name in bpy.data.objects:
            bpy.data.objects[name].hide_viewport = False
            bpy.data.objects[name].hide_render = False

    print("✓ Lighting: 4 act rigs (Act 1 active, others hidden)")


# ─────────────────────────────────────────────────────────────────────────────
# 7. COLOR SWATCH MATERIALS
# ─────────────────────────────────────────────────────────────────────────────

def setup_color_swatches():
    swatches = {
        # Act 1
        "A1_Gold_Light":   (1.000, 0.902, 0.502),
        "A1_Gold_Mid":     (0.957, 0.894, 0.757),
        "A1_Amber":        (0.831, 0.682, 0.275),
        "A1_Candlelight":  (1.000, 0.780, 0.000),
        # Act 2
        "A2_Blue_Light":   (0.659, 0.847, 0.941),
        "A2_Blue_Mid":     (0.482, 0.655, 0.773),
        "A2_Slate":        (0.290, 0.435, 0.647),
        "A2_Shadow":       (0.102, 0.122, 0.180),
        # Act 3
        "A3_Stone":        (0.482, 0.553, 0.631),
        "A3_Rain":         (0.608, 0.702, 0.800),
        "A3_Lamp":         (1.000, 0.702, 0.278),
        "A3_Dream":        (0.816, 0.784, 0.910),
        # Act 4
        "A4_Dawn_Light":   (0.961, 0.902, 0.827),
        "A4_Peach":        (0.957, 0.831, 0.639),
        "A4_Gold_Soft":    (1.000, 0.831, 0.639),
        "A4_Sky":          (0.439, 0.565, 0.753),
        # Characters
        "C_King_Skin":     (0.545, 0.388, 0.250),
        "C_King_Robe":     (0.545, 0.102, 0.102),
        "C_Taleju_Skin":   (0.831, 0.722, 0.533),
        "C_Taleju_Garment":(0.941, 0.910, 0.667),
        "C_Child_Dress":   (0.753, 0.063, 0.125),
        "C_Gold_Trim":     (0.831, 0.686, 0.216),
    }

    for name, rgb in swatches.items():
        if name in bpy.data.materials:
            bpy.data.materials.remove(bpy.data.materials[name])
        mat = bpy.data.materials.new(name)
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs["Base Color"].default_value = (*rgb, 1.0)

    print(f"✓ Materials: {len(swatches)} color swatches")


# ─────────────────────────────────────────────────────────────────────────────
# 8. REFERENCE OBJECTS
# ─────────────────────────────────────────────────────────────────────────────

def setup_reference_objects():
    ref_col = bpy.data.collections.get("Reference")

    def add_to_ref(obj):
        for col in list(obj.users_collection):
            col.objects.unlink(obj)
        ref_col.objects.link(obj)

    # Game table — cylinder built with bmesh (no operator context needed)
    if "REF_GameTable" not in bpy.data.objects:
        mesh = bpy.data.meshes.new("REF_GameTable_Mesh")
        bm = bmesh.new()
        bmesh.ops.create_circle(bm, cap_ends=True, cap_tris=False,
                                segments=32, radius=0.9)
        bmesh.ops.extrude_face_region(bm, geom=bm.faces[:])
        for v in bm.verts:
            if v.co.z > 0:
                v.co.z = 0.12
        bm.to_mesh(mesh)
        bm.free()
        table = bpy.data.objects.new("REF_GameTable", mesh)
        table.location = (0, 0, 0)
        bpy.context.scene.collection.objects.link(table)
        add_to_ref(table)
        mat = bpy.data.materials.get("C_Gold_Trim")
        if mat:
            table.data.materials.append(mat)

    # Floor plane — built with bmesh
    if "REF_Floor" not in bpy.data.objects:
        mesh = bpy.data.meshes.new("REF_Floor_Mesh")
        bm = bmesh.new()
        bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=8.0)
        bm.to_mesh(mesh)
        bm.free()
        floor = bpy.data.objects.new("REF_Floor", mesh)
        floor.location = (0, 0, 0)
        bpy.context.scene.collection.objects.link(floor)
        add_to_ref(floor)

    # Position markers — plain axes empties
    for emp_name, loc in [("REF_KingPosition", (-1.2, 0, 0)),
                          ("REF_TalejuPosition", (1.2, 0, 0))]:
        if emp_name not in bpy.data.objects:
            emp = bpy.data.objects.new(emp_name, None)
            emp.empty_display_type = 'CIRCLE'
            emp.empty_display_size = 0.5
            emp.location = Vector(loc)
            bpy.context.scene.collection.objects.link(emp)
            add_to_ref(emp)

    print("✓ Reference objects: floor, game table, character position markers")


# ─────────────────────────────────────────────────────────────────────────────
# 9. SHOT NAVIGATION PANEL (custom properties for easy reference)
# ─────────────────────────────────────────────────────────────────────────────

def setup_shot_index():
    """Store shot start frames as scene properties for quick navigation."""
    scene = bpy.context.scene
    for num, label, start, end, act, chars, cam in SHOTS:
        scene[f"shot_{num:02d}_start"] = start
        scene[f"shot_{num:02d}_end"]   = end
        scene[f"shot_{num:02d}_label"] = label
        scene[f"shot_{num:02d}_act"]   = act

    print("✓ Shot index stored in scene properties")
    print()
    print("  Jump to any shot by setting scene.frame_current:")
    for num, label, start, end, act, chars, cam in SHOTS:
        mins = (start - 1) // (24 * 60)
        secs = ((start - 1) // 24) % 60
        print(f"  Shot {num:02d} ({mins}:{secs:02d}) → frame {start:>5}  [{label}]")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print()
    print("=" * 68)
    print("  THE KING'S REGRET — Blender Scene Setup")
    print("=" * 68)
    print()

    setup_scene()
    setup_timeline_markers()
    shot_cols = setup_collections()
    setup_all_grease_pencil(shot_cols)
    setup_all_cameras(shot_cols)
    setup_lighting()
    setup_color_swatches()
    setup_reference_objects()
    setup_shot_index()

    print()
    print("=" * 68)
    print("  SETUP COMPLETE")
    print("=" * 68)
    print()
    print("QUICK START:")
    print("  1. Outliner → KingsRegret → Act1_GoldenEra → Shot_05_EyesMeeting_PEAK")
    print("  2. Select GP_S05_EyesMeeting_PEAK → enter Draw Mode (Tab)")
    print("  3. Active layer: CHAR_King  (draw the King's keypose first)")
    print("  4. Timeline marker S05 is at frame 1201 (0:50)")
    print("  5. Enable Act 1 lights: L1_Key, L1_Fill, L1_Rim")
    print()
    print("SHOT PRIORITIES:")
    print("  ★★★  Shot 05 — Eyes meeting   (Act 1 peak)")
    print("  ★★★  Shot 06 — Lighting shift  (transgression)")
    print("  ★★★  Shot 08 — Vanishing       (token falls)")
    print("  ★★★  Shot 15 — Kumari appears  (Act 4 peak)")
    print("  ★★   Shot 07, 09, 10, 11, 14")
    print("  ★    Shot 01, 02, 03, 04, 12, 13, 16, 17  (can simplify)")
    print()
    print("LAYER ORDER (bottom→top on each GP object):")
    print("  BG_Sky / BG_Architecture / BG_Props")
    print("  FX_Rain (Act 3 shots only)")
    print("  FX_Smoke")
    print("  CHAR_King / CHAR_Taleju / CHAR_Queen / CHAR_Child")
    print("  FX_Light")
    print()

main()
