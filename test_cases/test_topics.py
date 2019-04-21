import pytest
from all_api.topics import Topics
from utils import read_csv_file

index_page_Test_Data = read_csv_file('testdata/data.csv')
post_topic_data = read_csv_file('testdata/post_topic.csv')

@pytest.fixture
def get_topic_id():
    """
    fixture pytest的测试套件，可以作为基础操作方法被调用
    """
    url="/topics"
    t = Topics(url)
    r = t.post_create_topic("3333a0fb-6dd8-439e-813b-2c3a5213a154","11111111111","ask","xxxxxxxxxxxxx")
    print(r.json())
    res = r.json()
    topic_id = res['topic_id']
    return topic_id


def test_get_topic_detail(get_topic_id):
    print("get_topic_id===",get_topic_id)
    
    url = '/topic/'+get_topic_id
    t = Topics(url)
    r = t.get_topic_detail()
    print(r.json())


@pytest.mark.skip(reason="主要测试更新方法")
@pytest.mark.parametrize("limit,tab", index_page_Test_Data)
def test_index_page(limit,tab):
    url = "/topics"
    topics = Topics(url)
    # assert_limit=1
    # tab = 'ask'
    res = topics.get_index_topics(limit,tab)
    print("res==",res)
    r = res.json()
    assert len(r['data']) == int(limit)
    # r['data'][0]['tab'] == 'ask'
    assert res.status_code == 200
    all_data = r['data']
    for data in all_data:
        assert data['tab'] == tab



@pytest.mark.parametrize("token,title,tab,content", post_topic_data )
def test_post_topic(token,title,tab,content):
    url="/topics"
    t = Topics(url)
    r = t.post_create_topic(token,title,tab,content)
    print(r.json())
    res = r.json()
    topic_id = res['topic_id']
    print("topic_id====",topic_id)
    assert r.status_code == 200
    assert res['success'] == True

@pytest.mark.parametrize("token,title,tab,content",post_topic_data )
def test_update_topic(token, title,tab,content,get_topic_id):
    url="/topics/update"
    t = Topics(url)
    r = t.post_update_topic(token,get_topic_id, title+"00",tab,content+"11")
    print(r.json())

