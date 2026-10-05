import re

STOPWORDS = {
    "the", "and", "for", "with", "you", "your", "our", "are", "will", "have",
    "this", "that", "from", "they", "their", "has", "was", "were", "been",
    "into", "who", "what", "when", "where", "which", "about", "can", "all",
    "any", "not", "but", "such", "also", "etc", "using", "use", "used",
    "work", "working", "team", "teams", "experience", "years", "year",
    "ability", "strong", "good", "great", "new", "role", "job", "looking",
    "should", "must", "may", "per", "more", "other", "including",
    "we", "need", "needs", "skills", "skill", "responsibilities",
    "required", "preferred", "candidate", "knowledge", "understanding",
    "plus", "bonus", "excellent", "familiar",
}

def extract_keywords(text):
    words = re.findall(r"[a-z][a-z0-9+#]*", text.lower())
    return {word for word in words if len(word) > 1 and word not in STOPWORDS}

def match_resume(resume_text, job_text):
    job_keywords = extract_keywords(job_text)
    resume_keywords = extract_keywords(resume_text)

    matched = job_keywords & resume_keywords
    missing = job_keywords - resume_keywords
     
    if job_keywords:
        score = round(len(matched) / len(job_keywords) * 100)
    else:
        score = 0

    return{
        "score" : score,
        "matched" : sorted(matched),
        "missing" : sorted(missing),
    }