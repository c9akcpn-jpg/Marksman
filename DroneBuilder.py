import UnityPy
import os
import sys
import base64
import re

# ==========================================================
# DRONE VIEW EXACT BLOCKS GALAING SA IBINIGAY MO
# ==========================================================
DRONE_BLOCKS = {
    1: """      <SCameraCamp iId="1" fPosX="8.72" fPosY="-12.50" fPosZ="8.68" fRotX="42.86" fRotY="44.9" fRotZ="-0.07" fFov="0" fScreenPtCastDis="18"/>
      <SCameraCamp iId="2" fPosX="-8.72" fPosY="-12.50" fPosZ="-8.68" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="18"/>
      <SCameraCamp iId="3" fPosX="-8.72" fPosY="-12.50" fPosZ="-8.68" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="18"/>
      <SCameraCamp iId="4" fPosX="0.4" fPosY="-12.50" fPosZ="11.36" fRotX="45" fRotY="1.9" fRotZ="1.1" fScreenPtCastDis="18"/>
      <SCameraCamp iId="5" fPosX="-7" fPosY="-14" fPosZ="-10.75" fRotX="57" fRotY="-180" fRotZ="0" fScreenPtCastDis="15"/>
      <SCameraCamp iId="6" fPosX="9.47" fPosY="-36" fPosZ="-21.2" fRotX="55" fRotY="-180" fRotZ="0" fScreenPtCastDis="40"/>	
      <SCameraCamp iId="7" fPosX="-9.47" fPosY="-36" fPosZ="21.2" fRotX="55" fRotY="0" fRotZ="0" fScreenPtCastDis="40"/>		
      <SCameraCamp iId="8" fPosX="-6.54" fPosY="-17" fPosZ="-6.27" fRotX="60" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="15"/>
      <SCameraCamp iId="9" fPosX="8.96" fPosY="-13.50" fPosZ="8.96" fRotX="44.5" fRotY="44.9" fRotZ="-0.07" fScreenPtCastDis="42"/>
      <SCameraCamp iId="10" fPosX="-8.96" fPosY="-13.50" fPosZ="-8.96" fRotX="44.5" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="42"/>""",

    2: """      <SCameraCamp iId="1" fPosX="9.77" fPosY="-14.00" fPosZ="9.72" fRotX="42.86" fRotY="44.9" fRotZ="-0.07" fFov="0" fScreenPtCastDis="21"/>
      <SCameraCamp iId="2" fPosX="-9.77" fPosY="-14.00" fPosZ="-9.72" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="21"/>
      <SCameraCamp iId="3" fPosX="-9.77" fPosY="-14.00" fPosZ="-9.72" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="21"/>
      <SCameraCamp iId="4" fPosX="0.4" fPosY="-14.00" fPosZ="12.72" fRotX="45" fRotY="1.9" fRotZ="1.1" fScreenPtCastDis="21"/>
      <SCameraCamp iId="5" fPosX="-7" fPosY="-14" fPosZ="-10.75" fRotX="57" fRotY="-180" fRotZ="0" fScreenPtCastDis="15"/>
      <SCameraCamp iId="6" fPosX="9.47" fPosY="-36" fPosZ="-21.2" fRotX="55" fRotY="-180" fRotZ="0" fScreenPtCastDis="40"/>	
      <SCameraCamp iId="7" fPosX="-9.47" fPosY="-36" fPosZ="21.2" fRotX="55" fRotY="0" fRotZ="0" fScreenPtCastDis="40"/>		
      <SCameraCamp iId="8" fPosX="-6.54" fPosY="-17" fPosZ="-6.27" fRotX="60" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="15"/>
      <SCameraCamp iId="9" fPosX="9.96" fPosY="-15.00" fPosZ="9.96" fRotX="44.5" fRotY="44.9" fRotZ="-0.07" fScreenPtCastDis="45"/>
      <SCameraCamp iId="10" fPosX="-9.96" fPosY="-15.00" fPosZ="-9.96" fRotX="44.5" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="45"/>""",

    3: """      <SCameraCamp iId="1" fPosX="11.16" fPosY="-16.00" fPosZ="11.10" fRotX="42.86" fRotY="44.9" fRotZ="-0.07" fFov="0" fScreenPtCastDis="24"/>
      <SCameraCamp iId="2" fPosX="-11.16" fPosY="-16.00" fPosZ="-11.10" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="24"/>
      <SCameraCamp iId="3" fPosX="-11.16" fPosY="-16.00" fPosZ="-11.10" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="24"/>
      <SCameraCamp iId="4" fPosX="0.4" fPosY="-16.00" fPosZ="14.54" fRotX="45" fRotY="1.9" fRotZ="1.1" fScreenPtCastDis="24"/>
      <SCameraCamp iId="5" fPosX="-7" fPosY="-14" fPosZ="-10.75" fRotX="57" fRotY="-180" fRotZ="0" fScreenPtCastDis="15"/>
      <SCameraCamp iId="6" fPosX="9.47" fPosY="-36" fPosZ="-21.2" fRotX="55" fRotY="-180" fRotZ="0" fScreenPtCastDis="40"/>	
      <SCameraCamp iId="7" fPosX="-9.47" fPosY="-36" fPosZ="21.2" fRotX="55" fRotY="0" fRotZ="0" fScreenPtCastDis="40"/>		
      <SCameraCamp iId="8" fPosX="-6.54" fPosY="-17" fPosZ="-6.27" fRotX="60" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="15"/>
      <SCameraCamp iId="9" fPosX="11.28" fPosY="-17.00" fPosZ="11.28" fRotX="44.5" fRotY="44.9" fRotZ="-0.07" fScreenPtCastDis="48"/>
      <SCameraCamp iId="10" fPosX="-11.28" fPosY="-17.00" fPosZ="-11.28" fRotX="44.5" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="48"/>""",

    4: """      <SCameraCamp iId="1" fPosX="12.56" fPosY="-18.00" fPosZ="12.50" fRotX="42.86" fRotY="44.9" fRotZ="-0.07" fFov="0" fScreenPtCastDis="27"/>
      <SCameraCamp iId="2" fPosX="-12.56" fPosY="-18.00" fPosZ="-12.50" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="27"/>
      <SCameraCamp iId="3" fPosX="-12.56" fPosY="-18.00" fPosZ="-12.50" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="27"/>
      <SCameraCamp iId="4" fPosX="0.4" fPosY="-18.00" fPosZ="16.36" fRotX="45" fRotY="1.9" fRotZ="1.1" fScreenPtCastDis="27"/>
      <SCameraCamp iId="5" fPosX="-7" fPosY="-14" fPosZ="-10.75" fRotX="57" fRotY="-180" fRotZ="0" fScreenPtCastDis="15"/>
      <SCameraCamp iId="6" fPosX="9.47" fPosY="-36" fPosZ="-21.2" fRotX="55" fRotY="-180" fRotZ="0" fScreenPtCastDis="40"/>	
      <SCameraCamp iId="7" fPosX="-9.47" fPosY="-36" fPosZ="21.2" fRotX="55" fRotY="0" fRotZ="0" fScreenPtCastDis="40"/>		
      <SCameraCamp iId="8" fPosX="-6.54" fPosY="-17" fPosZ="-6.27" fRotX="60" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="15"/>
      <SCameraCamp iId="9" fPosX="12.61" fPosY="-19.00" fPosZ="12.61" fRotX="44.5" fRotY="44.9" fRotZ="-0.07" fScreenPtCastDis="50"/>
      <SCameraCamp iId="10" fPosX="-12.61" fPosY="-19.00" fPosZ="-12.61" fRotX="44.5" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="50"/>""",

    5: """      <SCameraCamp iId="1" fPosX="13.95" fPosY="-20.00" fPosZ="13.88" fRotX="42.86" fRotY="44.9" fRotZ="-0.07" fFov="0" fScreenPtCastDis="30"/>
      <SCameraCamp iId="2" fPosX="-13.95" fPosY="-20.00" fPosZ="-13.88" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="30"/>
      <SCameraCamp iId="3" fPosX="-13.95" fPosY="-20.00" fPosZ="-13.88" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="30"/>
      <SCameraCamp iId="4" fPosX="0.4" fPosY="-20.00" fPosZ="18.18" fRotX="45" fRotY="1.9" fRotZ="1.1" fScreenPtCastDis="30"/>
      <SCameraCamp iId="5" fPosX="-7" fPosY="-14" fPosZ="-10.75" fRotX="57" fRotY="-180" fRotZ="0" fScreenPtCastDis="15"/>
      <SCameraCamp iId="6" fPosX="9.47" fPosY="-36" fPosZ="-21.2" fRotX="55" fRotY="-180" fRotZ="0" fScreenPtCastDis="40"/>	
      <SCameraCamp iId="7" fPosX="-9.47" fPosY="-36" fPosZ="21.2" fRotX="55" fRotY="0" fRotZ="0" fScreenPtCastDis="40"/>		
      <SCameraCamp iId="8" fPosX="-6.54" fPosY="-17" fPosZ="-6.27" fRotX="60" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="15"/>
      <SCameraCamp iId="9" fPosX="13.94" fPosY="-21.00" fPosZ="13.94" fRotX="44.5" fRotY="44.9" fRotZ="-0.07" fScreenPtCastDis="52"/>
      <SCameraCamp iId="10" fPosX="-13.94" fPosY="-21.00" fPosZ="-13.94" fRotX="44.5" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="52"/>""",

    6: """      <SCameraCamp iId="1" fPosX="15.35" fPosY="-22.00" fPosZ="15.27" fRotX="42.86" fRotY="44.9" fRotZ="-0.07" fFov="0" fScreenPtCastDis="33"/>
      <SCameraCamp iId="2" fPosX="-15.35" fPosY="-22.00" fPosZ="-15.27" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="33"/>
      <SCameraCamp iId="3" fPosX="-15.35" fPosY="-22.00" fPosZ="-15.27" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="33"/>
      <SCameraCamp iId="4" fPosX="0.4" fPosY="-22.00" fPosZ="20.00" fRotX="45" fRotY="1.9" fRotZ="1.1" fScreenPtCastDis="33"/>
      <SCameraCamp iId="5" fPosX="-7" fPosY="-14" fPosZ="-10.75" fRotX="57" fRotY="-180" fRotZ="0" fScreenPtCastDis="15"/>
      <SCameraCamp iId="6" fPosX="9.47" fPosY="-36" fPosZ="-21.2" fRotX="55" fRotY="-180" fRotZ="0" fScreenPtCastDis="40"/>	
      <SCameraCamp iId="7" fPosX="-9.47" fPosY="-36" fPosZ="21.2" fRotX="55" fRotY="0" fRotZ="0" fScreenPtCastDis="40"/>		
      <SCameraCamp iId="8" fPosX="-6.54" fPosY="-17" fPosZ="-6.27" fRotX="60" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="15"/>
      <SCameraCamp iId="9" fPosX="15.27" fPosY="-23.00" fPosZ="15.27" fRotX="44.5" fRotY="44.9" fRotZ="-0.07" fScreenPtCastDis="55"/>
      <SCameraCamp iId="10" fPosX="-15.27" fPosY="-23.00" fPosZ="-15.27" fRotX="44.5" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="55"/>""",

    7: """      <SCameraCamp iId="1" fPosX="16.74" fPosY="-24.00" fPosZ="16.66" fRotX="42.86" fRotY="44.9" fRotZ="-0.07" fFov="0" fScreenPtCastDis="36"/>
      <SCameraCamp iId="2" fPosX="-16.74" fPosY="-24.00" fPosZ="-16.66" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="36"/>
      <SCameraCamp iId="3" fPosX="-16.74" fPosY="-24.00" fPosZ="-16.66" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="36"/>
      <SCameraCamp iId="4" fPosX="0.4" fPosY="-24.00" fPosZ="21.81" fRotX="45" fRotY="1.9" fRotZ="1.1" fScreenPtCastDis="36"/>
      <SCameraCamp iId="5" fPosX="-7" fPosY="-14" fPosZ="-10.75" fRotX="57" fRotY="-180" fRotZ="0" fScreenPtCastDis="15"/>
      <SCameraCamp iId="6" fPosX="9.47" fPosY="-36" fPosZ="-21.2" fRotX="55" fRotY="-180" fRotZ="0" fScreenPtCastDis="40"/>	
      <SCameraCamp iId="7" fPosX="-9.47" fPosY="-36" fPosZ="21.2" fRotX="55" fRotY="0" fRotZ="0" fScreenPtCastDis="40"/>		
      <SCameraCamp iId="8" fPosX="-6.54" fPosY="-17" fPosZ="-6.27" fRotX="60" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="15"/>
      <SCameraCamp iId="9" fPosX="16.60" fPosY="-25.00" fPosZ="16.60" fRotX="44.5" fRotY="44.9" fRotZ="-0.07" fScreenPtCastDis="58"/>
      <SCameraCamp iId="10" fPosX="-16.60" fPosY="-25.00" fPosZ="-16.60" fRotX="44.5" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="58"/>""",

    8: """      <SCameraCamp iId="1" fPosX="18.14" fPosY="-26.00" fPosZ="18.05" fRotX="42.86" fRotY="44.9" fRotZ="-0.07" fFov="0" fScreenPtCastDis="39"/>
      <SCameraCamp iId="2" fPosX="-18.14" fPosY="-26.00" fPosZ="-18.05" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="39"/>
      <SCameraCamp iId="3" fPosX="-18.14" fPosY="-26.00" fPosZ="-18.05" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="39"/>
      <SCameraCamp iId="4" fPosX="0.4" fPosY="-26.00" fPosZ="23.63" fRotX="45" fRotY="1.9" fRotZ="1.1" fScreenPtCastDis="39"/>
      <SCameraCamp iId="5" fPosX="-7" fPosY="-14" fPosZ="-10.75" fRotX="57" fRotY="-180" fRotZ="0" fScreenPtCastDis="15"/>
      <SCameraCamp iId="6" fPosX="9.47" fPosY="-36" fPosZ="-21.2" fRotX="55" fRotY="-180" fRotZ="0" fScreenPtCastDis="40"/>	
      <SCameraCamp iId="7" fPosX="-9.47" fPosY="-36" fPosZ="21.2" fRotX="55" fRotY="0" fRotZ="0" fScreenPtCastDis="40"/>		
      <SCameraCamp iId="8" fPosX="-6.54" fPosY="-17" fPosZ="-6.27" fRotX="60" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="15"/>
      <SCameraCamp iId="9" fPosX="17.92" fPosY="-27.00" fPosZ="17.92" fRotX="44.5" fRotY="44.9" fRotZ="-0.07" fScreenPtCastDis="61"/>
      <SCameraCamp iId="10" fPosX="-17.92" fPosY="-27.00" fPosZ="-17.92" fRotX="44.5" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="61"/>""",

    9: """      <SCameraCamp iId="1" fPosX="19.53" fPosY="-28.00" fPosZ="19.44" fRotX="42.86" fRotY="44.9" fRotZ="-0.07" fFov="0" fScreenPtCastDis="42"/>
      <SCameraCamp iId="2" fPosX="-19.53" fPosY="-28.00" fPosZ="-19.44" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="42"/>
      <SCameraCamp iId="3" fPosX="-19.53" fPosY="-28.00" fPosZ="-19.44" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="42"/>
      <SCameraCamp iId="4" fPosX="0.4" fPosY="-28.00" fPosZ="25.45" fRotX="45" fRotY="1.9" fRotZ="1.1" fScreenPtCastDis="42"/>
      <SCameraCamp iId="5" fPosX="-7" fPosY="-14" fPosZ="-10.75" fRotX="57" fRotY="-180" fRotZ="0" fScreenPtCastDis="15"/>
      <SCameraCamp iId="6" fPosX="9.47" fPosY="-36" fPosZ="-21.2" fRotX="55" fRotY="-180" fRotZ="0" fScreenPtCastDis="40"/>	
      <SCameraCamp iId="7" fPosX="-9.47" fPosY="-36" fPosZ="21.2" fRotX="55" fRotY="0" fRotZ="0" fScreenPtCastDis="40"/>		
      <SCameraCamp iId="8" fPosX="-6.54" fPosY="-17" fPosZ="-6.27" fRotX="60" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="15"/>
      <SCameraCamp iId="9" fPosX="19.25" fPosY="-29.00" fPosZ="19.25" fRotX="44.5" fRotY="44.9" fRotZ="-0.07" fScreenPtCastDis="64"/>
      <SCameraCamp iId="10" fPosX="-19.25" fPosY="-29.00" fPosZ="-19.25" fRotX="44.5" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="64"/>""",

    10: """      <SCameraCamp iId="1" fPosX="20.93" fPosY="-30.00" fPosZ="20.82" fRotX="42.86" fRotY="44.9" fRotZ="-0.07" fFov="0" fScreenPtCastDis="45"/>
      <SCameraCamp iId="2" fPosX="-20.93" fPosY="-30.00" fPosZ="-20.82" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="45"/>
      <SCameraCamp iId="3" fPosX="-20.93" fPosY="-30.00" fPosZ="-20.82" fRotX="42.86" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="45"/>
      <SCameraCamp iId="4" fPosX="0.4" fPosY="-30.00" fPosZ="27.27" fRotX="45" fRotY="1.9" fRotZ="1.1" fScreenPtCastDis="45"/>
      <SCameraCamp iId="5" fPosX="-7" fPosY="-14" fPosZ="-10.75" fRotX="57" fRotY="-180" fRotZ="0" fScreenPtCastDis="15"/>
      <SCameraCamp iId="6" fPosX="9.47" fPosY="-36" fPosZ="-21.2" fRotX="55" fRotY="-180" fRotZ="0" fScreenPtCastDis="40"/>	
      <SCameraCamp iId="7" fPosX="-9.47" fPosY="-36" fPosZ="21.2" fRotX="55" fRotY="0" fRotZ="0" fScreenPtCastDis="40"/>		
      <SCameraCamp iId="8" fPosX="-6.54" fPosY="-17" fPosZ="-6.27" fRotX="60" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="15"/>
      <SCameraCamp iId="9" fPosX="20.58" fPosY="-31.00" fPosZ="20.58" fRotX="44.5" fRotY="44.9" fRotZ="-0.07" fScreenPtCastDis="67"/>
      <SCameraCamp iId="10" fPosX="-20.58" fPosY="-31.00" fPosZ="-20.58" fRotX="44.5" fRotY="-134.1" fRotZ="-0.07" fScreenPtCastDis="67"/>"""
}

# ==========================================================
# MAIN AUTOMATION SCRIPT
# ==========================================================
def build_drone_views():
    original_file = "Document.unity3d"
    
    if not os.path.exists(original_file):
        print(f"❌ Hindi nahanap ang {original_file} sa folder na ito!")
        print("Siguraduhin na nandito ang original UnityFS file bago i-run.")
        return

    print(f"🚀 Binubuksan ang {original_file}...")
    env = UnityPy.load(original_file)
    
    is_found = False
    
    for obj in env.objects:
        if obj.type.name == "TextAsset":
            data = obj.read()
            name = getattr(data, "name", getattr(data, "m_Name", ""))
            
            if "battlesystem" in name.lower():
                is_found = True
                print(f"✅ Nakita ang target: {name}")
                
                # --- EXTRACT & DECODE STEP ---
                content = getattr(data, "script", getattr(data, "m_Script", None))
                if content is None or len(content) == 0:
                    content = getattr(data, "text", getattr(data, "m_Text", b""))
                
                if isinstance(content, str):
                    content = content.encode('utf-8')
                    
                try:
                    xml_bytes = base64.b64decode(content)
                    xml_str = xml_bytes.decode('utf-8', errors='ignore')
                except Exception as e:
                    print(f"❌ Error sa pag-decode ng Base64: {e}")
                    return

                # --- CLEANUP (Delete existing ID 1 to 10) ---
                clean_xml = re.sub(r'[ \t]*<SCameraCamp\s+iId="(1|2|3|4|5|6|7|8|9|10)"[^>]*/>\r?\n?', '', xml_str)

                # Hanapin kung saan isisingit ang bagong codes
                match = re.search(r'(<SCamera iIndex="1"[^>]*>\r?\n?)', clean_xml)
                if not match:
                    print("❌ Hindi nahanap ang <SCamera iIndex=\"1\"> sa loob ng XML.")
                    return
                insert_pos = match.end()

                print("\n⚙️  Gumagawa na ng 1x hanggang 10x files. Pakihintay...\n")

                # --- MODIFY, ENCODE & REPACK STEP (Loop 1x to 10x) ---
                for level in range(1, 11):
                    # I-inject ang specific block (1x, 2x, etc.)
                    new_xml = clean_xml[:insert_pos] + DRONE_BLOCKS[level] + "\n" + clean_xml[insert_pos:]
                    
                    # I-encode pabalik sa Base64
                    encoded_bytes = base64.b64encode(new_xml.encode('utf-8'))
                    
                    # DITO ANG FIX: I-convert ang bytes sa string para sa UnityPy TextAsset
                    encoded_str = encoded_bytes.decode('utf-8') 
                    
                    # I-apply ang changes sa Unity TextAsset object
                    if hasattr(data, "script"):
                        data.script = encoded_str
                    elif hasattr(data, "m_Script"):
                        data.m_Script = encoded_str
                    elif hasattr(data, "text"):
                        data.text = encoded_str
                    elif hasattr(data, "m_Text"):
                        data.m_Text = encoded_str
                        
                    data.save()
                    
                    # I-save ang buong bundle gamit ang bagong pangalan
                    out_name = f"Document.unity3d{level}x"
                    with open(out_name, "wb") as f:
                        f.write(env.file.save())
                        
                    print(f"✔️  Na-repack na ang: {out_name}")
                
                print("\n🎉 SUCCESS! Ang lahat ng files mula 1x hanggang 10x ay handa na sa folder mo.")
                return
                
    if not is_found:
        print("❌ Hindi nahanap ang 'battlesystem' TextAsset sa loob ng Document.unity3d.")

if __name__ == "__main__":
    build_drone_views()
