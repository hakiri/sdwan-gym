import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='sdwan-v0',
    entry_point='gym_sdwan.envs:SdwanEnv',
)

