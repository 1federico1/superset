# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from typing import List

import sqlalchemy.sql.sqltypes

from superset.utils.data import add_data, ColumnInfo

COLUMN_TYPES = [
    sqlalchemy.sql.sqltypes.INTEGER(),
    sqlalchemy.sql.sqltypes.VARCHAR(length=255),
    sqlalchemy.sql.sqltypes.TEXT(),
    sqlalchemy.sql.sqltypes.BOOLEAN(),
    sqlalchemy.sql.sqltypes.FLOAT(),
    sqlalchemy.sql.sqltypes.DATE(),
    sqlalchemy.sql.sqltypes.TIME(),
    sqlalchemy.sql.sqltypes.DATETIME(),
]


def load_big_data() -> None:
    # create table with 100 columns to test SQL Lab
    columns: List[ColumnInfo] = []
    for i in range(100):
        column: ColumnInfo = {
            "name": f"col{i}",
            "type": COLUMN_TYPES[i % len(COLUMN_TYPES)],
            "nullable": False,
            "default": None,
            "autoincrement": "auto",
            "primary_key": 1 if i == 0 else 0,
        }
        columns.append(column)

    add_data(columns=columns, num_rows=1000, table_name="wide_table")
