# -*- coding: utf-8 -*-
#
# This file is part of INSPIRE.
# Copyright (C) 2016 CERN.
#
# INSPIRE is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from __future__ import absolute_import, division, print_function

from flask import current_app
from mock import patch

from inspirehep.utils.url import make_user_agent_string


@patch('inspirehep.utils.url.__version__', '0.1.0')
def test_make_user_agent_string():
    """Test that user agent is created."""
    config = {'SERVER_NAME': 'http://inspirehep.net'}

    with patch.dict(current_app.config, config):
        user_agent = make_user_agent_string()
        assert user_agent == "InspireHEP-0.1.0 (+http://inspirehep.net;)"

        user_agent_with_component = make_user_agent_string("submission")
        assert user_agent_with_component == "InspireHEP-0.1.0 (+http://inspirehep.net;) [submission]"
