def score_applicant(education, experience, gender, age):
    
    education_scores = {
        'highschool': 10,
        'bachelor': 20,
        'master': 30,
        'phd': 40
    }
    score = education_scores.get(education.lower(), 0)

    # Experience scoring
    score += min(experience, 20) * 2  # Max 40 points for experience

    # Age scoring (prefer 22-60)
    if 22 <= age <= 60:
        score += 10
    else:
        score += 0


    return score

# Example usage
applicant = {
    'education': 'master',
    'experience': 5,
    'gender': 'female',
    'age': 30
}
print("Applicant Score:", score_applicant(**applicant))