# coding: utf-8
import hashlib
import json
import logging

from redash.query_runner import register
from redash.query_runner.big_query import BigQuery
import six

from .matcher import find_include_japanese_column
logger = logging.getLogger(__name__)


class BigQueryJP(BigQuery):
    @classmethod
    def type(cls):
        return "bigquery_jp"

    def run_query(self, query, user):
        logging.info('query_reply : bq_jp :  %s', query)
        def escape(s):
            return six.u("_") + hashlib.md5(s.encode("utf-8")).hexdigest()

        escape_table = {
            escape(japanese): japanese
            for japanese in find_include_japanese_column(query)
        }
        logging.info('query_reply : bq_jp :  %s', escape_table)

        for escaped, raw in six.iteritems(escape_table):
            query = query.replace(raw, escaped)

        logging.info('query_encode : bq_jp :  %s', query)
        json_data, error = super(BigQueryJP, self).run_query(query, user)
        if error is not None:
            return None, error

        data = json.loads(json_data)
        data["rows"] = [
            {escape_table.get(col, col): val for col, val in six.iteritems(row)}
            for row in data["rows"]
        ]
        for column in data["columns"]:
            name = column["name"]
            if name in escape_table:
                original_name = escape_table.get(name, name)
                column["name"] = original_name
                column["friendly_name"] = original_name
        return json.dumps(data), None


register(BigQueryJP)
