
# File: openai_agents_sdk (manual version)
# Yeh file Agent aur Tool decorators ka dummy version hai
# Jis se aap bina actual SDK ke project run horaha hai
# agent() aur tool() decorators sirf class ko wapas return kar rahe hain
# Real SDK na ho to structure break na ho, is liye yeh zaroori hai


class Agent:
    pass

def agent(name, description):
    def decorator(cls):
        return cls
    return decorator

class Tool:
    pass

def tool(name, description):
    def decorator(cls):
        return cls
    return decorator