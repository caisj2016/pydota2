# NOTE: This code is to a large degree based on DeepMind work for 
#       AI in StarCraft2, just ported towards the Dota 2 game.
#       DeepMind's License is posted below.

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#            http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A random agent for Dota2."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy

from pydota2.agents import base_agent
from pydota2.lib import actions


class Agent(base_agent.BaseAgent):
    """
       A hero select agent for Dota2.
    """

    def step(self, obs):
        super(Agent, self).step(obs)
        
        return []