{
    "timestamp":1637660765732,
    "webhookEvent":"jira:issue_updated",
    "issue_event_type_name":"issue_commented",
    "user":{
        "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
        "name":"B180093",
        "key":"b180093",
        "emailAddress":"bluenote212@telechips.com",
        "avatarUrls":{
        "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
        "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
        "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
        "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
        },
        "displayName":"신호찬 (Chance H Shin)",
        "active":true,
        "timeZone":"Asia/Seoul"
    },
    "issue":{
        "id":"108789",
        "self":"https://tcs.telechips.com:8443/rest/api/2/issue/108789",
        "key":"TMTPD-4137",
        "fields":{
            "issuetype":{
                
            },"self":"https://tcs.telechips.com:8443/rest/api/2/issuetype/11004",
                "id":"11004",
                "description":"팀 프로젝트에서 연구 업무를 위한 Issue type",
                "iconUrl":"https://tcs.telechips.com:8443/secure/viewavatar?size=xsmall&avatarId=10318&avatarType=issuetype",
                "name":"연구",
                "subtask":false,
                "avatarId":10318
            "timespent":null,
            "project":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/project/10107",
                "id":"10107",
                "key":"TMTPD",
                "name":"RND Innovation Team",
                "avatarUrls":{
                "48x48":"https://tcs.telechips.com:8443/secure/projectavatar?avatarId=10324",
                "24x24":"https://tcs.telechips.com:8443/secure/projectavatar?size=small&avatarId=10324",
                "16x16":"https://tcs.telechips.com:8443/secure/projectavatar?size=xsmall&avatarId=10324",
                "32x32":"https://tcs.telechips.com:8443/secure/projectavatar?size=medium&avatarId=10324"
                },
                "projectCategory":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/projectCategory/10000",
                "id":"10000",
                "description":"팀별 Task를 관리하기 위한 프로젝트",
                "name":"RnD-팀 프로젝트"
                }
            },
            "fixVersions":[
            ],
            "customfield_11200":null,
            "aggregatetimespent":null,
            "resolution":null,
            "customfield_10302":null,
            "resolutiondate":null,
            "customfield_10628":"Proxy to Checklist Checklist",
            "workratio":-1,
            "lastViewed":"2021-11-23T18:40:23.115+0900",
            "watches":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/issue/TMTPD-4137/watchers",
                "watchCount":0,
                "isWatching":false
            },
            "created":"2021-11-23T10:25:40.350+0900",
            "customfield_12000":null,
            "customfield_12001":null,
            "priority":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/priority/3",
                "iconUrl":"https://tcs.telechips.com:8443/images/icons/priorities/medium_2.svg",
                "name":"Medium",
                "id":"3"
            },
            "customfield_10100":"0|i0gab3:",
            "customfield_10101":null,
            "customfield_10102":null,
            "customfield_10300":null,
            "labels":[
            ],
            "customfield_11702":null,
            "customfield_11900":null,
            "customfield_11704":null,
            "timeestimate":null,
            "aggregatetimeoriginalestimate":null,
            "versions":[
            ],
            "customfield_11706":null,
            "customfield_11705":null,
            "customfield_11903":null,
            "customfield_11708":null,
            "customfield_11707":null,
            "issuelinks":[
            ],
            "customfield_11709":null,
            "assignee":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                "name":"B180093",
                "key":"b180093",
                "emailAddress":"bluenote212@telechips.com",
                "avatarUrls":{
                "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                },
                "displayName":"신호찬 (Chance H Shin)",
                "active":true,
                "timeZone":"Asia/Seoul"
            },
            "updated":"2021-11-23T18:40:22.977+0900",
            "status":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/status/3",
                "description":"This issue is being actively worked on at the moment by the assignee.",
                "iconUrl":"https://tcs.telechips.com:8443/images/icons/statuses/inprogress.png",
                "name":"In Progress",
                "id":"3",
                "statusCategory":{
                    "self":"https://tcs.telechips.com:8443/rest/api/2/statuscategory/4",
                    "id":4,
                    "key":"indeterminate",
                    "colorName":"yellow",
                    "name":"In Progress"
                }
            },
            "components":[
            ],
            "timeoriginalestimate":null,
            "description":"* 연구원들이 실제 사용하는 서비스가 됨에 따라 back up 구성 필요\r\n* 테스트 베드를 구축하여 테스트는 테스트 베드에서만 할 수 있도록 구성\r\n* docx 파일 pdf 로 변환 가능한지도 테스트 배드 구축 후 적용 예정\r\n* 서비스 안정화를 위해 config 별도 분리 및 시스템 고도화 필요\r\n* 로그를 남길 수 있는지 확인 필요",
            "customfield_11101":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/customFieldOption/11305",
                "value":"Not related to Chip",
                "id":"11305"
            },
            "timetracking":{
            },
            "customfield_10687":null,
            "customfield_10644":null,
            "customfield_10689":null,
            "attachment":[
            ],
            "aggregatetimeestimate":null,
            "summary":"Flask 서버 Back 구성, 테스트 베드 구축, 시스템 고도화",
            "creator":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                "name":"B180093",
                "key":"b180093",
                "emailAddress":"bluenote212@telechips.com",
                "avatarUrls":{
                    "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                    "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                    "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                    "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                },
                "displayName":"신호찬 (Chance H Shin)",
                "active":true,
                "timeZone":"Asia/Seoul"
            },
            "subtasks":[
            ],
            "reporter":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                "name":"B180093",
                "key":"b180093",
                "emailAddress":"bluenote212@telechips.com",
                "avatarUrls":{
                    "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                    "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                    "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                    "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                },
                "displayName":"신호찬 (Chance H Shin)",
                "active":true,
                "timeZone":"Asia/Seoul"
            },
            "customfield_10000":"{summaryBean=com.atlassian.jira.plugin.devstatus.rest.SummaryBean@24c6c98f[summary={pullrequest=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@73ef3137[overall=com.atlassian.jira.plugin.devstatus.summary.beans.PullRequestOverallBean@54889ee2[stateCount=0,state=OPEN,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], build=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@26b34eac[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BuildOverallBean@34ab7144[failedBuildCount=0,successfulBuildCount=0,unknownBuildCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], review=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@3ec7886f[overall=com.atlassian.jira.plugin.devstatus.summary.beans.ReviewsOverallBean@2e286edb[stateCount=0,state=<null>,dueDate=<null>,overDue=false,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], deployment-environment=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@1252839c[overall=com.atlassian.jira.plugin.devstatus.summary.beans.DeploymentOverallBean@7d9ce1c3[topEnvironments=[],showProjects=false,successfulCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], repository=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@7f9a9aef[overall=com.atlassian.jira.plugin.devstatus.summary.beans.CommitOverallBean@12a96d71[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], branch=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@14e152db[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BranchOverallBean@ee92b7d[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}]},errors=[],configErrors=[]], devSummaryJson={\"cachedValue\":{\"errors\":[],\"configErrors\":[],\"summary\":{\"pullrequest\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":\"OPEN\",\"open\":true},\"byInstanceType\":{}},\"build\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"failedBuildCount\":0,\"successfulBuildCount\":0,\"unknownBuildCount\":0},\"byInstanceType\":{}},\"review\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":null,\"dueDate\":null,\"overDue\":false,\"completed\":false},\"byInstanceType\":{}},\"deployment-environment\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"topEnvironments\":[],\"showProjects\":false,\"successfulCount\":0},\"byInstanceType\":{}},\"repository\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}},\"branch\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}}}},\"isStale\":false}}",
            "aggregateprogress":{
                "progress":0,
                "total":0
            },
            "customfield_10200":"2021-11-23",
            "customfield_10684":null,
            "customfield_10685":null,
            "customfield_10686":null,
            "environment":null,
            "customfield_10711":null,
            "customfield_11800":null,
            "customfield_11726":null,
            "duedate":"2021-12-03",
            "progress":{
                "progress":0,
                "total":0
            },
            "comment":{
            "comments":[
            {
                "self":"https://tcs.telechips.com:8443/rest/api/2/issue/108789/comment/249373",
                "id":"249373",
                "author":{
                    "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                    "name":"B180093",
                    "key":"b180093",
                    "emailAddress":"bluenote212@telechips.com",
                    "avatarUrls":{
                        "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                        "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                        "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                        "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                    },
                    "displayName":"신호찬 (Chance H Shin)",
                    "active":true,
                    "timeZone":"Asia/Seoul"
                },
                "body":"tcs",
                "updateAuthor":{
                        "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                        "name":"B180093",
                        "key":"b180093",
                        "emailAddress":"bluenote212@telechips.com",
                        "avatarUrls":{
                        "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                        "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                        "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                        "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                    },
                    "displayName":"신호찬 (Chance H Shin)",
                    "active":true,
                    "timeZone":"Asia/Seoul"
                },
                "created":"2021-11-23T18:18:26.107+0900",
                "updated":"2021-11-23T18:18:26.107+0900"
            },
            {
                "self":"https://tcs.telechips.com:8443/rest/api/2/issue/108789/comment/249374",
                "id":"249374",
                "author":{
                    "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                    "name":"B180093",
                    "key":"b180093",
                    "emailAddress":"bluenote212@telechips.com",
                    "avatarUrls":{
                        "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                        "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                        "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                        "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                    },
                    "displayName":"신호찬 (Chance H Shin)",
                    "active":true,
                    "timeZone":"Asia/Seoul"
                },
                "body":"tcsffffgg",
                "updateAuthor":{
                    "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                    "name":"B180093",
                    "key":"b180093",
                    "emailAddress":"bluenote212@telechips.com",
                    "avatarUrls":{
                        "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                        "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                        "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                        "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                    },
                    "displayName":"신호찬 (Chance H Shin)",
                    "active":true,
                    "timeZone":"Asia/Seoul"
                },
                "created":"2021-11-23T18:18:58.017+0900",
                "updated":"2021-11-23T18:20:54.790+0900"
            },
            {
                "self":"https://tcs.telechips.com:8443/rest/api/2/issue/108789/comment/249375",
                "id":"249375",
                "author":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                    "name":"B180093",
                    "key":"b180093",
                    "emailAddress":"bluenote212@telechips.com",
                    "avatarUrls":{
                        "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                        "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                        "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                        "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                    },
                    "displayName":"신호찬 (Chance H Shin)",
                    "active":true,
                    "timeZone":"Asia/Seoul"
            },
            "body":"test",
            "updateAuthor":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                "name":"B180093",
                "key":"b180093",
                "emailAddress":"bluenote212@telechips.com",
                "avatarUrls":{
                    "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                    "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                    "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                    "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                },
                "displayName":"신호찬 (Chance H Shin)",
                "active":true,
                "timeZone":"Asia/Seoul"
            },
            "created":"2021-11-23T18:21:23.083+0900",
            "updated":"2021-11-23T18:21:23.083+0900"
            },
            {
                "self":"https://tcs.telechips.com:8443/rest/api/2/issue/108789/comment/249376",
                "id":"249376",
                "author":{
                    "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                    "name":"B180093",
                    "key":"b180093",
                    "emailAddress":"bluenote212@telechips.com",
                    "avatarUrls":{
                        "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                        "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                        "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                        "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                },
                "displayName":"신호찬 (Chance H Shin)",
                "active":true,
                "timeZone":"Asia/Seoul"
            },
            "body":"dddd",
            "updateAuthor":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                "name":"B180093",
                "key":"b180093",
                "emailAddress":"bluenote212@telechips.com",
                "avatarUrls":{
                    "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                    "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                    "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                    "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
            },
            "displayName":"신호찬 (Chance H Shin)",
            "active":true,
            "timeZone":"Asia/Seoul"
            },
            "created":"2021-11-23T18:24:40.023+0900",
            "updated":"2021-11-23T18:24:40.023+0900"
            },
            {
                "self":"https://tcs.telechips.com:8443/rest/api/2/issue/108789/comment/249378",
                "id":"249378",
                "author":{
                    "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                    "name":"B180093",
                    "key":"b180093",
                    "emailAddress":"bluenote212@telechips.com",
                    "avatarUrls":{
                        "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                        "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                        "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                        "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                },
                "displayName":"신호찬 (Chance H Shin)",
                "active":true,
                "timeZone":"Asia/Seoul"
            },
            "body":"test do it do it do it do it do it do it do it do it do it",
            "updateAuthor":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                "name":"B180093",
                "key":"b180093",
                "emailAddress":"bluenote212@telechips.com",
                "avatarUrls":{
                    "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                    "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                    "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                    "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                },
                "displayName":"신호찬 (Chance H Shin)",
                "active":true,
                "timeZone":"Asia/Seoul"
            },
            "created":"2021-11-23T18:34:35.407+0900",
            "updated":"2021-11-23T18:34:35.407+0900"
            },
            {
            "self":"https://tcs.telechips.com:8443/rest/api/2/issue/108789/comment/249381",
            "id":"249381",
            "author":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                "name":"B180093",
                "key":"b180093",
                "emailAddress":"bluenote212@telechips.com",
                "avatarUrls":{
                    "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                    "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                    "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                    "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                },
                "displayName":"신호찬 (Chance H Shin)",
                "active":true,
                "timeZone":"Asia/Seoul"
            },
            "body":"test do it do it do it do it do it do it do it do it do ittest do it do it do it do it do it do it do it do it do ittest do it do it do it do it do it do it do it do it do ittest do it do it do it do it do it do it do it do it do ittest do it do it do it do it do it do it do it do it do ittest do it do it do it do it do it do it do it do it do ittest do it do it do it do it do it do it do it do it do it",
            "updateAuthor":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                "name":"B180093",
                "key":"b180093",
                "emailAddress":"bluenote212@telechips.com",
                "avatarUrls":{
                    "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                    "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                    "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                    "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                },
                "displayName":"신호찬 (Chance H Shin)",
                "active":true,
                "timeZone":"Asia/Seoul"
            },
            "created":"2021-11-23T18:40:22.977+0900",
            "updated":"2021-11-23T18:40:22.977+0900"
            },
            {
            "self":"https://tcs.telechips.com:8443/rest/api/2/issue/108789/comment/249384",
            "id":"249384",
            "author":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                "name":"B180093",
                "key":"b180093",
                "emailAddress":"bluenote212@telechips.com",
                "avatarUrls":{
                    "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                    "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                    "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                    "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                },
                "displayName":"신호찬 (Chance H Shin)",
                "active":true,
                "timeZone":"Asia/Seoul"
            },
            "body":"dd",
            "updateAuthor":{
                "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                "name":"B180093",
                "key":"b180093",
                "emailAddress":"bluenote212@telechips.com",
                "avatarUrls":{
                    "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                    "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                    "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                    "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                },
                "displayName":"신호찬 (Chance H Shin)",
                "active":true,
                "timeZone":"Asia/Seoul"
            },
            "created":"2021-11-23T18:46:05.707+0900",
            "updated":"2021-11-23T18:46:05.707+0900"
            }
            ],
            "maxResults":7,
            "total":7,
            "startAt":0
            },
            "worklog":{
            "startAt":0,
            "maxResults":20,
            "total":0,
            "worklogs":[
            ]
            }
        }
    },
    "comment":{
        "self":"https://tcs.telechips.com:8443/rest/api/2/issue/108789/comment/249384",
        "id":"249384",
        "author":{
            "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
            "name":"B180093",
            "key":"b180093",
            "emailAddress":"bluenote212@telechips.com",
            "avatarUrls":{
                "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
            },
            "displayName":"신호찬 (Chance H Shin)",
            "active":true,
            "timeZone":"Asia/Seoul"
        },
        "body":"dd",
        "updateAuthor":{
            "self":"https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
            "name":"B180093",
            "key":"b180093",
            "emailAddress":"bluenote212@telechips.com",
            "avatarUrls":{
                "48x48":"https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                "24x24":"https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                "16x16":"https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                "32x32":"https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
            },
            "displayName":"신호찬 (Chance H Shin)",
            "active":true,
            "timeZone":"Asia/Seoul"
        },
        "created":"2021-11-23T18:46:05.706+0900",
        "updated":"2021-11-23T18:46:05.706+0900"
    }
}