from django.contrib.auth.tokens import PasswordResetTokenGenerator

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, signature, timestamp):
        return (
            signature.email + str(timestamp)
        )
