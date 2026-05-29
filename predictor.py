def predict_health(glucose, haemoglobin, cholesterol):

    risks = []

    if glucose > 140:
        risks.append("Possible Diabetes Risk")

    if haemoglobin < 12:
        risks.append("Possible Anemia Risk")

    if cholesterol > 200:
        risks.append("Possible Heart Disease Risk")

    if not risks:
        return "No Significant Risk Detected"

    return ", ".join(risks)
