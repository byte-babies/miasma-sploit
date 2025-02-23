import itertools
import base64

strs = [
"TLOhPc5G",
"5ZEOKOaT",
"D8mYRpEx",
"JF729NWc",
"iBSgsTXy",
"2V1idHPN" 
]

def print_base64_permutations(strs):
    for perm in itertools.permutations(strs):
        combined_str = ''.join(perm)
        print(combined_str)
        try:
            decoded_str = base64.b64decode(combined_str).decode('utf-8')
            print(decoded_str)
        except Exception as e:
            pass
            #print(f"Decoding failed for {combined_str}: {e}")

print_base64_permutations(strs)
