from pxr import Usd
import sys

def list_prims(usd_path):
    print(f"Opening: {usd_path}\n")
    stage = Usd.Stage.Open(usd_path)
    if not stage:
        print("ERROR: Cannot open USD.")
        return
    cameras, arts, xforms, meshes = [], [], [], []
    for prim in stage.Traverse():
        path = str(prim.GetPath())
        ptype = prim.GetTypeName()
        row = (path, ptype)
        if   ptype == "Camera":           cameras.append(row)
        elif "Articulation" in ptype:     arts.append(row)
        elif ptype == "Xform":            xforms.append(row)
        elif ptype == "Mesh":             meshes.append(row)
    for label, group, lim in [
        ("=== CAMERAS ===",       cameras, 999),
        ("=== ARTICULATIONS ===", arts,    999),
        ("=== XFORMS (50) ===",   xforms,   50),
        ("=== MESHES (30) ===",   meshes,   30),
    ]:
        print(f"\n{label}")
        for p,t in group[:lim]:
            print(f"  {p:<65} {t}")
    print(f"\nTOTAL: {sum(1 for _ in stage.Traverse())} prims")

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: python list_usd_prims.py <scene.usd>")
        sys.exit(1)
    list_prims(sys.argv[1])
