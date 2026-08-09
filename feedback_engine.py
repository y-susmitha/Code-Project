class FeedbackEngine:

    def __init__(self, config):

        self.config = config

        self.feedback = config.get("feedback", {})

    def get_feedback(self, stage):

        if stage in self.feedback:

            return self.feedback[stage].get(
                "message",
                ""
            )

        return ""

    def get_feedback_by_status(self, status):

        return self.get_feedback(status)
