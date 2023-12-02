from app.models.setting_basic import SettingBasic
from app.models.setting_pro import SettingPro
from config import GRADE


def getGitConfigList(tenantID, appID, hideToken=True):
    obj = SettingBasic() if GRADE == "base" else SettingPro()
    return obj.getGitConfigList(tenantID, appID, hideToken=hideToken)

def getCIConfigList(tenantID, appID, hideToken=True):
    obj = SettingBasic() if GRADE == "base" else SettingPro()
    return obj.getCIConfigList(tenantID, appID, hideToken=hideToken)

def getCDConfigList(tenantID, appID, hideToken=True):
    obj = SettingBasic() if GRADE == "base" else SettingPro()
    return obj.getCDConfigList(tenantID, appID, hideToken=hideToken)

def getLLMConfigList(tenantID, appID):
    obj = SettingBasic() if GRADE == "base" else SettingPro()
    return obj.getLLMConfigList(tenantID, appID)