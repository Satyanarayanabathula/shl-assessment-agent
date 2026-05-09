from app.retriever import retrieve_assessments



def is_vague_query(user_message):

    vague_phrases = [
        "need assessment",
        "need test",
        "looking for assessment",
        "help me hire"
    ]

    user_message = user_message.lower()

    for phrase in vague_phrases:
        if phrase in user_message:
            return True

    if len(user_message.split()) < 4:
        return True

    return False
def is_off_topic(user_message):

    allowed_keywords = [
        "assessment",
        "test",
        "hiring",
        "developer",
        "engineer",
        "manager",
        "java",
        "python",
        "skills",
        "candidate",
        "job",
        "finance",
        "accounting",
        "backend",
        "frontend",
        "api"
    ]

    user_message = user_message.lower()

    for keyword in allowed_keywords:
        if keyword in user_message:
            return False

    return True
def is_comparison_query(user_message):

    comparison_words = [
        "compare",
        "difference",
        "vs",
        "versus"
    ]

    user_message = user_message.lower()

    for word in comparison_words:
        if word in user_message:
            return True

    return False
def generate_reply(messages):

    latest_message = messages[-1].content

    conversation_text = " ".join(
        [message.content for message in messages]
    )

    # off-topic detection
    if is_off_topic(latest_message):

        return {
            "reply": (
                "I can only help with SHL assessments, "
                "hiring, candidate evaluation, and job-role recommendations."
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # comparison queries
    if is_comparison_query(latest_message):

        comparison_results = retrieve_assessments(
            latest_message,
            top_k=2
        )

        comparison_recommendations = []

        for result in comparison_results:
            comparison_recommendations.append({
                "name": result["name"],
                "url": result["url"],
                "test_type": "Comparison Candidate",
                "reason": (
                    "This assessment is relevant "
                    "to the requested comparison query."
                )
            })

        return {
            "reply": (
                "Here are relevant SHL assessments "
                "you can compare based on role fit, "
                "skills measured, and technical focus."
            ),
            "recommendations": comparison_recommendations,
            "end_of_conversation": False
        }


# check vague query
    if is_vague_query(latest_message):

        return {
            "reply": (
                "Can you share more details about the role, "
                "skills required, seniority level, "
                "or personality traits you want to assess?"
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # retrieve recommendations
    results = retrieve_assessments(
        conversation_text,
        top_k=5
    )
    recommendations = []

    for result in results:

        test_type = "General"

        name_lower = result["name"].lower()

        if "java" in name_lower or ".net" in name_lower:
            test_type = "Technical"

        elif "manager" in name_lower:
            test_type = "Managerial"

        elif "account" in name_lower:
            test_type = "Finance"
        recommendations.append({
            "name": result["name"],
            "url": result["url"],
            "test_type": test_type,
            "reason": (
                f"This assessment matches the "
                f"requested skills and hiring requirements."
            )
        })
    return {
        "reply":(
    f"I found {len(recommendations)} SHL assessments "
    f"that align with your hiring requirements."
),

        "recommendations": recommendations,
        "end_of_conversation": False
    }
