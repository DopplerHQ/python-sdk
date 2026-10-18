import json

import pytest
import responses
from http_exceptions import ClientException

from dopplersdk import DopplerSDK
from dopplersdk.models.DeleteRequest import DeleteRequest
from dopplersdk.net.http_client import HTTPClient


@pytest.mark.parametrize("as_model", [False, True])
@pytest.mark.parametrize("statuses", [[200], [503, 200], [400]])
@responses.activate
def test_project_delete_sends_body_on_every_attempt(monkeypatch, as_model, statuses):
    monkeypatch.setattr("dopplersdk.net.http_client.sleep", lambda _: None)
    url = "https://api.doppler.com/v3/projects/project"
    for status in statuses:
        responses.delete(url, json={"success": status == 200}, status=status)
    payload = DeleteRequest(project="project-example") if as_model else {"project": "project-example"}
    client = DopplerSDK(access_token="test-token")
    if statuses[-1] == 400:
        with pytest.raises(ClientException):
            client.projects.delete(payload)
    else:
        assert client.projects.delete(payload) == {"success": True}
    assert len(responses.calls) == len(statuses)
    for call in responses.calls:
        assert json.loads(call.request.body or "null") == {"project": "project-example"}
        assert call.request.headers["Content-Type"] == "application/json"


@pytest.mark.parametrize("retry,statuses", [(True, [503, 200]), (False, [200])])
@responses.activate
def test_legacy_bodyless_delete_positional_retry(monkeypatch, retry, statuses):
    monkeypatch.setattr("dopplersdk.net.http_client.sleep", lambda _: None)
    url = "https://api.doppler.com/bodyless"
    for status in statuses:
        responses.delete(url, json={}, status=status)
    assert HTTPClient(None).delete(url, {}, retry) == {}
    assert len(responses.calls) == len(statuses)
    assert all(call.request.body is None for call in responses.calls)


@responses.activate
def test_get_remains_bodyless():
    url = "https://api.doppler.com/bodyless"
    responses.get(url, json={}, status=200)
    assert HTTPClient(None).get(url, {}) == {}
    assert responses.calls[0].request.body is None
