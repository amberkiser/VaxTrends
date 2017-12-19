#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script will import all the data for the SQLite database.
@author: amberkiser
"""
from import_data import import_coverage, import_incidence_rate, import_history

import_coverage.import_coverage_data()
import_incidence_rate.import_rate_data()
import_history.import_history_data()
