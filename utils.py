import re

def detect_fillers(transcript):
    fillers = r'\b(umm|uh|like|you know|basically|actually|sort of|right|so)\b'
    matches = re.findall(fillers, transcript.lower())
    count = len(matches)
    
    if count > 0:
        return f"⚠️ Detected {count} filler words: {', '.join(set(matches))[:3]}... Reduce them to boost your score by 20%!"
    else:
        return "✅ No fillers detected – Great delivery!"
