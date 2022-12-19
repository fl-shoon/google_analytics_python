from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    Dimension,
    Metric,
    DateRange,
    RunReportRequest
)

def sample_run_report(property_id):
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property = f"properties/{property_id}",
        dimensions = [Dimension(name="fileName")],
        metrics = [Metric(name="eventCount")],
        date_ranges = [DateRange(start_date="2022-11-01", end_date="today")],
    )
    response = client.run_report(request)
    # print(response)

    for row in response.rows:
        print(row.dimension_values[0].value)
        print(row.metric_values[0].value)

property_id = "312806931"
sample_run_report(property_id)