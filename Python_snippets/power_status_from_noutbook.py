def check_Power():
    class SYSTEM_POWER_STATUS(ctypes.Structure):
        _fields_ = [
            ('ACLineStatus', wintypes.BYTE),
            ('BatteryFlag', wintypes.BYTE),
            ('BatteryLifePercent', wintypes.BYTE),
            ('Reserved1', wintypes.BYTE),
            ('BatteryLifeTime', wintypes.DWORD),
            ('BatteryFullLifeTime', wintypes.DWORD),
        ]

    SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)

    GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
    GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
    GetSystemPowerStatus.restype = wintypes.BOOL

    status = SYSTEM_POWER_STATUS()
    if not GetSystemPowerStatus(ctypes.pointer(status)):
        raise ctypes.WinError()
    if status.ACLineStatus != 0:
        # print('Power Ok!')
        lbl_Power_sensor['text'] = 'Power sensor status: AC power connected, Ok'
    else:
        # print('No Power')
        lbl_Power_sensor['text'] = 'Power sensor status: AC power lost, Battery mode!'
    # print('ACLineStatus', status.ACLineStatus)
    # print('BatteryFlag', status.BatteryFlag)
    # print('BatteryLifePercent', status.BatteryLifePercent)
    # print('BatteryLifeTime', status.BatteryLifeTime)
    # print('BatteryFullLifeTime', status.BatteryFullLifeTime)
    root.after(30000, check_Power)