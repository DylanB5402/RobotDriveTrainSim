import enum

class ErrorCode(enum.IntEnum):
    OK = 0
    OKAY = 0
    CAN_MSG_STALE = 1
    CAN_TX_FULL = -1
    TxFailed = -1
    InvalidParamValue = -2
    CAN_INVALID_PARAM = -2
    RxTimeout = -3
    CAN_MSG_NOT_FOUND = -3
    TxTimeout = -4
    CAN_NO_MORE_TX_JOBS = -4
    UnexpectedArbId = -5
    CAN_NO_SESSIONS_AVAIL = -5
    BufferFull = +6
    CAN_OVERFLOW = -6
    SensorNotPresent = -7
    FirmwareTooOld = -8
    CouldNotChangePeriod = -9
    GeneralError = -100
    GENERAL_ERROR = -100
    SIG_NOT_UPDATED = -200
    SigNotUpdated = -200
    NotAllPIDValuesUpdated = -201
    GEN_PORT_ERROR = -300
    PORT_MODULE_TYPE_MISMATCH = -301
    GEN_MODULE_ERROR = -400
    MODULE_NOT_INIT_SET_ERROR = -401
    MODULE_NOT_INIT_GET_ERROR = -402
    WheelRadiusTooSmall = -500
    TicksPerRevZero = -501
    DistanceBetweenWheelsTooSmall = -502
    GainsAreNotSet = -503
    IncompatibleMode = -600
    InvalidHandle = -601
    FeatureRequiresHigherFirm = -700
    TalonFeatureRequiresHigherFirm = -701
    PulseWidthSensorNotPresent = 10
    GeneralWarning = 100
    FeatureNotSupported = 101
    NotImplemented = 102
    FirmVersionCouldNotBeRetrieved = 103
    FeaturesNotAvailableYet = 104
    ControlModeNotValid = 105
    ControlModeNotSupportedYet = 106
    CascadedPIDNotSupporteYet = 107
    AuxiliaryPIDNotSupportedYet = 107
    RemoteSensorsNotSupportedYet = 108
    MotProfFirmThreshold = 109
    MotProfFirmThreshold2 = 110

class ParamEnum(enum.IntEnum):
    eOnBoot_BrakeMode = 31
    eQuadFilterEn = 91
    eQuadIdxPolarity = 108
    eClearPositionOnIdx = 100
    eMotionProfileHasUnderrunErr = 119
    eMotionProfileTrajectoryPointDurationMs = 120
    eClearPosOnLimitF = 144
    eClearPosOnLimitR = 145
    eStatusFramePeriod = 300
    eOpenloopRamp = 301
    eClosedloopRamp = 302
    eNeutralDeadband = 303
    ePeakPosOutput = 305
    eNominalPosOutput = 306
    ePeakNegOutput = 307
    eNominalNegOutput = 308
    eProfileParamSlot_P = 310
    eProfileParamSlot_I = 311
    eProfileParamSlot_D = 312
    eProfileParamSlot_F = 313
    eProfileParamSlot_IZone = 314
    eProfileParamSlot_AllowableErr = 315
    eProfileParamSlot_MaxIAccum = 316
    eProfileParamSlot_PeakOutput = 317
    eClearPositionOnLimitF = 320
    eClearPositionOnLimitR = 321
    eClearPositionOnQuadIdx = 322
    eSampleVelocityPeriod = 325
    eSampleVelocityWindow = 326
    eFeedbackSensorType = 330
    eSelectedSensorPosition = 331
    eFeedbackNotContinuous = 332
    eRemoteSensorSource = 333
    eRemoteSensorDeviceID = 334
    eSensorTerm = 335
    eRemoteSensorClosedLoopDisableNeutralOnLOS = 336
    ePIDLoopPolarity = 337
    ePIDLoopPeriod = 338
    eSelectedSensorCoefficient = 339
    eForwardSoftLimitThreshold = 340
    eReverseSoftLimitThreshold = 341
    eForwardSoftLimitEnable = 342
    eReverseSoftLimitEnable = 343
    eNominalBatteryVoltage = 350
    eBatteryVoltageFilterSize = 351
    eContinuousCurrentLimitAmps = 360
    ePeakCurrentLimitMs = 361
    ePeakCurrentLimitAmps = 362
    eClosedLoopIAccum = 370
    eCustomParam = 380
    eStickyFaults = 390
    eAnalogPosition = 400
    eQuadraturePosition = 401
    ePulseWidthPosition = 402
    eMotMag_Accel = 410
    eMotMag_VelCruise = 411
    eLimitSwitchSource = 421
    eLimitSwitchNormClosedAndDis = 422
    eLimitSwitchDisableNeutralOnLOS = 423
    eLimitSwitchRemoteDevID = 424
    eSoftLimitDisableNeutralOnLOS = 425
    ePulseWidthPeriod_EdgesPerRot = 430
    ePulseWidthPeriod_FilterWindowSz = 431
    eYawOffset = 160
    eCompassOffset = 161
    eBetaGain = 162
    eEnableCompassFusion = 163
    eGyroNoMotionCal = 164
    eEnterCalibration = 165
    eFusedHeadingOffset = 166
    eStatusFrameRate = 169
    eAccumZ = 170
    eTempCompDisable = 171
    eMotionMeas_tap_threshX = 172
    eMotionMeas_tap_threshY = 173
    eMotionMeas_tap_threshZ = 174
    eMotionMeas_tap_count = 175
    eMotionMeas_tap_time = 176
    eMotionMeas_tap_time_multi = 177
    eMotionMeas_shake_reject_thresh = 178
    eMotionMeas_shake_reject_time = 179
    eMotionMeas_shake_reject_timeout = 180

class CANifierControlFrame(enum.IntEnum):
    CANifier_Control_1_General = 50593792
    CANifier_Control_2_PwmOutput = 50593856

class CANifierStatusFrame(enum.IntEnum):
    Status_1_General = 267264
    Status_2_General = 267328
    Status_3_PwmInputs0 = 267392
    Status_4_PwmInputs1 = 267456
    Status_5_PwmInputs2 = 267520
    Status_6_PwmInputs3 = 267584
    Status_8_Misc = 267712

class GeneralPin(enum.IntEnum):
    QUAD_IDX = 0
    QUAD_B = 1
    QUAD_A = 2
    LIMR = 3
    LIMF = 4
    SDA = 5
    SCL = 6
    SPI_CS = 7
    SPI_MISO_PWM2P = 8
    SPI_MOSI_PWM1P = 9
    SPI_CLK_PWM0P = 10

class SetValueMotionProfile(enum.IntEnum):
    Disable = 0
    Enable = 1
    Hold = 2

class TrajectoryDuration(enum.IntEnum):
    T0ms = 0
    T5ms = 5
    T10ms = 10
    T20ms = 20
    T30ms = 30
    T40ms = 40
    T50ms = 50
    T100ms = 100

class ControlFrame(enum.IntEnum):
    Control_3_General = 262272
    Control_4_Advanced = 262336
    Control_6_MotProfAddTrajPoint = 262464
class ControlFrameEnhanced(enum.IntEnum):
    Control_3_General_ = 262272
    Control_4_Advanced_ = 262336
    Control_5_FeedbackOutputOverride_ = 262400
    Control_6_MotProfAddTrajPoint_ = 262464

class ControlMode(enum.IntEnum):
    PercentOutput = 0
    Position = 1
    Velocity = 2
    Current = 3
    Follower = 5
    MotionProfile = 6
    MotionMagic = 7
    MotionProfileArc = 10
    Disabled = 15

class DemandType(enum.IntEnum):
    Neutral = 0
    AuxPID = 1
    ArbitraryFeedForward = 2

class FeedbackDevice(enum.IntEnum):
    None_ = -1
    QuadEncoder = 0
    Analog = 2
    Tachometer = 4
    PulseWidthEncodedPosition = 8
    SensorSum = 9
    SensorDifference = 10
    RemoteSensor0 = 11
    RemoteSensor1 = 12
    SoftwareEmulatedSensor = 15
    CTRE_MagEncoder_Absolute = PulseWidthEncodedPosition
    CTRE_MagEncoder_Relative = QuadEncoder
class RemoteFeedbackDevice(enum.IntEnum):
    None_ = -1
    SensorSum = 9
    SensorDifference = 10
    RemoteSensor0 = 11
    RemoteSensor1 = 12
    SoftwareEmulatedSensor = 15

class FollowerType(enum.IntEnum):
    PercentOutput = 0
    AuxOutput1 = 1

class LimitSwitchSource(enum.IntEnum):
    FeedbackConnector = 0
    RemoteTalonSRX = 1
    RemoteCANifier = 2
    Deactivated = 3
class RemoteLimitSwitchSource(enum.IntEnum):
    RemoteTalonSRX = 1
    RemoteCANifier = 2
    Deactivated = 3
class LimitSwitchNormal(enum.IntEnum):
    NormallyOpen = 0
    NormallyClosed = 1
    Disabled = 2

class NeutralMode(enum.IntEnum):
    EEPROMSetting = 0
    Coast = 1
    Brake = 2

class RemoteSensorSource(enum.IntEnum):
    Off = 0
    TalonSRX_SelectedSensor = 1
    Pigeon_Yaw = 2
    Pigeon_Pitch = 3
    Pigeon_Roll = 4
    CANifier_Quadrature = 5
    CANifier_PWMInput0 = 6
    CANifier_PWMInput1 = 7
    CANifier_PWMInput2 = 8
    CANifier_PWMInput3 = 9
    GadgeteerPigeon_Yaw = 10
    GadgeteerPigeon_Pitch = 11
    GadgeteerPigeon_Roll = 12

class SensorTerm(enum.IntEnum):
    Sum0 = 0
    Sum1 = 1
    Diff0 = 2
    Diff1 = 3

class StatusFrameEnhanced(enum.IntEnum):
    Status_1_General = 5120
    Status_2_Feedback0 = 5184
    Status_4_AinTempVbat = 5312
    Status_6_Misc = 5440
    Status_7_CommStatus = 5504
    Status_9_MotProfBuffer = 5632
    Status_10_MotionMagic = 5696
    Status_10_Targets = 5696
    Status_12_Feedback1 = 5824
    Status_13_Base_PIDF0 = 5888
    Status_14_Turn_PIDF1 = 5952
    Status_15_FirmareApiStatus = 6016
    Status_3_Quadrature = 5248
    Status_8_PulseWidth = 5568
    Status_11_UartGadgeteer = 5760
class StatusFrame(enum.IntEnum):
    Status_1_General_ = 5120
    Status_2_Feedback0_ = 5184
    Status_4_AinTempVbat_ = 5312
    Status_6_Misc_ = 5440
    Status_7_CommStatus_ = 5504
    Status_9_MotProfBuffer_ = 5632
    Status_10_MotionMagic_ = 5696
    Status_10_Targets_ = 5696
    Status_12_Feedback1_ = 5824
    Status_13_Base_PIDF0_ = 5888
    Status_14_Turn_PIDF1_ = 5952
    Status_15_FirmareApiStatus_ = 6016

class VelocityMeasPeriod(enum.IntEnum):
    Period_1Ms = 1
    Period_2Ms = 2
    Period_5Ms = 5
    Period_10Ms = 10
    Period_20Ms = 20
    Period_25Ms = 25
    Period_50Ms = 50
    Period_100Ms = 100

class PigeonIMU_ControlFrame(enum.IntEnum):
    CondStatus_Control_1 = 272384

class PigeonIMU_StatusFrame(enum.IntEnum):
    CondStatus_1_General = 270336
    CondStatus_9_SixDeg_YPR = 270848
    CondStatus_6_SensorFusion = 270656
    CondStatus_11_GyroAccum = 270976
    CondStatus_2_GeneralCompass = 270400
    CondStatus_3_GeneralAccel = 270464
    CondStatus_10_SixDeg_Quat = 270912
    RawStatus_4_Mag = 269504
    BiasedStatus_2_Gyro = 269376
    BiasedStatus_4_Mag = 269504
    BiasedStatus_6_Accel = 269632

