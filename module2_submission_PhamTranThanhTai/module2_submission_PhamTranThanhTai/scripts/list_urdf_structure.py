import xml.etree.ElementTree as ET
import sys

def list_urdf(urdf_path):
    print(f"Reading URDF: {urdf_path}\n")
    root = ET.parse(urdf_path).getroot()
    print(f"Robot name: {root.attrib.get('name','unknown')}")

    links = root.findall("link")
    print(f"\n=== LINKS ({len(links)}) ===")
    for l in links:
        name = l.attrib.get("name","?")
        v = l.find("visual") is not None
        c = l.find("collision") is not None
        i = l.find("inertial") is not None
        print(f"  {name:<45} visual={v} col={c} inertial={i}")

    joints = root.findall("joint")
    print(f"\n=== JOINTS ({len(joints)}) ===")
    print(f"  {'NAME':<45} {'TYPE':<12} {'PARENT':<30} CHILD  [limit]")
    print("  " + "-"*110)
    for j in joints:
        name  = j.attrib.get("name","?")
        jtype = j.attrib.get("type","?")
        p = j.find("parent"); c = j.find("child")
        pname = p.attrib.get("link","?") if p is not None else "?"
        cname = c.attrib.get("link","?") if c is not None else "?"
        lim = j.find("limit")
        lstr = f"[{lim.attrib.get('lower','?')}, {lim.attrib.get('upper','?')}]" if lim is not None else ""
        print(f"  {name:<45} {jtype:<12} {pname:<30} {cname}  {lstr}")

    types = {}
    for j in joints:
        t = j.attrib.get("type","?")
        types[t] = types.get(t,0)+1
    print(f"\n=== SUMMARY: {len(links)} links, {len(joints)} joints ===")
    for t,c in sorted(types.items()):
        print(f"  {t}: {c}")

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: python list_urdf_structure.py <robot.urdf>")
        sys.exit(1)
    list_urdf(sys.argv[1])
