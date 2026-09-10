class MockAI:
    def generate(self,prompt):
        return {"text":f"Mock response for: {prompt[:60]}","provider":"mock"}
def valid_structured(result,required):
    return all(k in result for k in required)
