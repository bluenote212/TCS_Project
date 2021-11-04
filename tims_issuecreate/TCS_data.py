{
    "_id" : ObjectId("6078ee0e31250d867675b48c"),
    "data" : {
        "timestamp" : NumberLong(1618537997239),
        "webhookEvent" : "jira:issue_updated",
        "issue_event_type_name" : "issue_reopened",
        "user" : {
            "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
            "name" : "B180093",
            "key" : "b180093",
            "emailAddress" : "bluenote212@telechips.com",
            "avatarUrls" : {
                "48x48" : "https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                "24x24" : "https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                "16x16" : "https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                "32x32" : "https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
            },
            "displayName" : "신호찬 (Chance H Shin)",
            "active" : true,
            "timeZone" : "Asia/Seoul"
        },
        "issue" : {
            "id" : "91867",
            "self" : "https://tcs.telechips.com:8443/rest/api/2/issue/91867",
            "key" : "TMTPD-3762",
            "fields" : {
                "issuetype" : {
                    "self" : "https://tcs.telechips.com:8443/rest/api/2/issuetype/11004",
                    "id" : "11004",
                    "description" : "팀 프로젝트에서 연구 업무를 위한 Issue type",
                    "iconUrl" : "https://tcs.telechips.com:8443/secure/viewavatar?size=xsmall&avatarId=10318&avatarType=issuetype",
                    "name" : "연구",
                    "subtask" : false,
                    "avatarId" : 10318
                },
                "timespent" : null,
                "project" : {
                    "self" : "https://tcs.telechips.com:8443/rest/api/2/project/10107",
                    "id" : "10107",
                    "key" : "TMTPD",
                    "name" : "RND Innovation Team",
                    "avatarUrls" : {
                        "48x48" : "https://tcs.telechips.com:8443/secure/projectavatar?avatarId=10324",
                        "24x24" : "https://tcs.telechips.com:8443/secure/projectavatar?size=small&avatarId=10324",
                        "16x16" : "https://tcs.telechips.com:8443/secure/projectavatar?size=xsmall&avatarId=10324",
                        "32x32" : "https://tcs.telechips.com:8443/secure/projectavatar?size=medium&avatarId=10324"
                    },
                    "projectCategory" : {
                        "self" : "https://tcs.telechips.com:8443/rest/api/2/projectCategory/10000",
                        "id" : "10000",
                        "description" : "팀별 Task를 관리하기 위한 프로젝트",
                        "name" : "RnD-팀 프로젝트"
                    }
                },
                "fixVersions" : [],
                "customfield_11200" : null,
                "aggregatetimespent" : null,
                "resolution" : null,
                "customfield_10302" : null,
                "resolutiondate" : null,
                "customfield_10628" : "Proxy to Checklist Checklist",
                "workratio" : -1,
                "lastViewed" : "2021-04-16T10:53:17.195+0900",
                "watches" : {
                    "self" : "https://tcs.telechips.com:8443/rest/api/2/issue/TMTPD-3762/watchers",
                    "watchCount" : 1,
                    "isWatching" : false
                },
                "created" : "2021-03-26T18:04:28.890+0900",
                "priority" : {
                    "self" : "https://tcs.telechips.com:8443/rest/api/2/priority/3",
                    "iconUrl" : "https://tcs.telechips.com:8443/images/icons/priorities/medium_2.svg",
                    "name" : "Medium",
                    "id" : "3"
                },
                "customfield_10100" : "0|i0dgxj:",
                "customfield_10101" : null,
                "customfield_10102" : null,
                "customfield_10300" : null,
                "labels" : [],
                "customfield_11702" : null,
                "customfield_11900" : null,
                "customfield_11704" : null,
                "timeestimate" : null,
                "aggregatetimeoriginalestimate" : null,
                "versions" : [],
                "customfield_11706" : null,
                "customfield_11705" : null,
                "customfield_11708" : null,
                "customfield_11707" : null,
                "issuelinks" : [],
                "customfield_11709" : null,
                "assignee" : {
                    "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                    "name" : "B180093",
                    "key" : "b180093",
                    "emailAddress" : "bluenote212@telechips.com",
                    "avatarUrls" : {
                        "48x48" : "https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                        "24x24" : "https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                        "16x16" : "https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                        "32x32" : "https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                    },
                    "displayName" : "신호찬 (Chance H Shin)",
                    "active" : true,
                    "timeZone" : "Asia/Seoul"
                },
                "updated" : "2021-04-16T10:53:17.233+0900",
                "status" : {
                    "self" : "https://tcs.telechips.com:8443/rest/api/2/status/4",
                    "description" : "This issue was once resolved, but the resolution was deemed incorrect. From here issues are either marked assigned or resolved.",
                    "iconUrl" : "https://tcs.telechips.com:8443/images/icons/statuses/reopened.png",
                    "name" : "Reopen",
                    "id" : "4",
                    "statusCategory" : {
                        "self" : "https://tcs.telechips.com:8443/rest/api/2/statuscategory/4",
                        "id" : 4,
                        "key" : "indeterminate",
                        "colorName" : "yellow",
                        "name" : "In Progress"
                    }
                },
                "components" : [],
                "timeoriginalestimate" : null,
                "description" : "첨부파일 테스트\r\n\r\n!이미지 1.png!",
                "customfield_11101" : {
                    "self" : "https://tcs.telechips.com:8443/rest/api/2/customFieldOption/11305",
                    "value" : "Not related to Chip",
                    "id" : "11305"
                },
                "timetracking" : {},
                "customfield_10687" : null,
                "customfield_10644" : null,
                "customfield_10689" : null,
                "attachment" : [ 
                    {
                        "self" : "https://tcs.telechips.com:8443/rest/api/2/attachment/58901",
                        "id" : "58901",
                        "filename" : "이미지 1.png",
                        "author" : {
                            "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                            "name" : "B180093",
                            "key" : "b180093",
                            "emailAddress" : "bluenote212@telechips.com",
                            "avatarUrls" : {
                                "48x48" : "https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                                "24x24" : "https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                                "16x16" : "https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                                "32x32" : "https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                            },
                            "displayName" : "신호찬 (Chance H Shin)",
                            "active" : true,
                            "timeZone" : "Asia/Seoul"
                        },
                        "created" : "2021-04-15T10:36:49.537+0900",
                        "size" : 53658,
                        "mimeType" : "image/png",
                        "content" : "https://tcs.telechips.com:8443/secure/attachment/58901/%EC%9D%B4%EB%AF%B8%EC%A7%80+1.png",
                        "thumbnail" : "https://tcs.telechips.com:8443/secure/thumbnail/58901/_thumb_58901.png"
                    }
                ],
                "aggregatetimeestimate" : null,
                "summary" : "테스트",
                "creator" : {
                    "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                    "name" : "B180093",
                    "key" : "b180093",
                    "emailAddress" : "bluenote212@telechips.com",
                    "avatarUrls" : {
                        "48x48" : "https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                        "24x24" : "https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                        "16x16" : "https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                        "32x32" : "https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                    },
                    "displayName" : "신호찬 (Chance H Shin)",
                    "active" : true,
                    "timeZone" : "Asia/Seoul"
                },
                "subtasks" : [],
                "reporter" : {
                    "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                    "name" : "B180093",
                    "key" : "b180093",
                    "emailAddress" : "bluenote212@telechips.com",
                    "avatarUrls" : {
                        "48x48" : "https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                        "24x24" : "https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                        "16x16" : "https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                        "32x32" : "https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                    },
                    "displayName" : "신호찬 (Chance H Shin)",
                    "active" : true,
                    "timeZone" : "Asia/Seoul"
                },
                "customfield_10000" : "{summaryBean=com.atlassian.jira.plugin.devstatus.rest.SummaryBean@29d6f04b[summary={pullrequest=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@21e2af3b[overall=com.atlassian.jira.plugin.devstatus.summary.beans.PullRequestOverallBean@109d3f72[stateCount=0,state=OPEN,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], build=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@48e185c[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BuildOverallBean@1ac4f42e[failedBuildCount=0,successfulBuildCount=0,unknownBuildCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], review=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@2eeb0b3a[overall=com.atlassian.jira.plugin.devstatus.summary.beans.ReviewsOverallBean@57f4c73a[stateCount=0,state=<null>,dueDate=<null>,overDue=false,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], deployment-environment=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@234c7960[overall=com.atlassian.jira.plugin.devstatus.summary.beans.DeploymentOverallBean@1e948ca3[topEnvironments=[],showProjects=false,successfulCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], repository=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@6850e690[overall=com.atlassian.jira.plugin.devstatus.summary.beans.CommitOverallBean@196c31b7[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], branch=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@592bdc83[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BranchOverallBean@6360b291[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}]},errors=[],configErrors=[]], devSummaryJson={\"cachedValue\":{\"errors\":[],\"configErrors\":[],\"summary\":{\"pullrequest\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":\"OPEN\",\"open\":true},\"byInstanceType\":{}},\"build\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"failedBuildCount\":0,\"successfulBuildCount\":0,\"unknownBuildCount\":0},\"byInstanceType\":{}},\"review\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":null,\"dueDate\":null,\"overDue\":false,\"completed\":false},\"byInstanceType\":{}},\"deployment-environment\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"topEnvironments\":[],\"showProjects\":false,\"successfulCount\":0},\"byInstanceType\":{}},\"repository\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}},\"branch\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}}}},\"isStale\":false}}",
                "aggregateprogress" : {
                    "progress" : 0,
                    "total" : 0
                },
                "customfield_10200" : "2021-03-26",
                "customfield_10684" : null,
                "customfield_10685" : null,
                "customfield_10686" : null,
                "environment" : null,
                "customfield_10711" : null,
                "customfield_11800" : null,
                "customfield_11726" : null,
                "duedate" : "2021-03-26",
                "progress" : {
                    "progress" : 0,
                    "total" : 0
                },
                "comment" : {
                    "comments" : [ 
                        {
                            "self" : "https://tcs.telechips.com:8443/rest/api/2/issue/91867/comment/208729",
                            "id" : "208729",
                            "author" : {
                                "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=rnd_rest_api_account",
                                "name" : "rnd_rest_api_account",
                                "key" : "rndadmin",
                                "emailAddress" : "bluenote212@telechips.com",
                                "avatarUrls" : {
                                    "48x48" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=48",
                                    "24x24" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=24",
                                    "16x16" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=16",
                                    "32x32" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=32"
                                },
                                "displayName" : "rnd_rest_api_account",
                                "active" : true,
                                "timeZone" : "Asia/Seoul"
                            },
                            "body" : "SUCCESS: Integrated in Jenkins build chance_test #9 (See [https://jenkins-rnd.telechips.com:8443/job/chance_test/9/])\n",
                            "updateAuthor" : {
                                "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=rnd_rest_api_account",
                                "name" : "rnd_rest_api_account",
                                "key" : "rndadmin",
                                "emailAddress" : "bluenote212@telechips.com",
                                "avatarUrls" : {
                                    "48x48" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=48",
                                    "24x24" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=24",
                                    "16x16" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=16",
                                    "32x32" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=32"
                                },
                                "displayName" : "rnd_rest_api_account",
                                "active" : true,
                                "timeZone" : "Asia/Seoul"
                            },
                            "created" : "2021-04-14T13:46:46.387+0900",
                            "updated" : "2021-04-14T13:46:46.387+0900"
                        }, 
                        {
                            "self" : "https://tcs.telechips.com:8443/rest/api/2/issue/91867/comment/208730",
                            "id" : "208730",
                            "author" : {
                                "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=rnd_rest_api_account",
                                "name" : "rnd_rest_api_account",
                                "key" : "rndadmin",
                                "emailAddress" : "bluenote212@telechips.com",
                                "avatarUrls" : {
                                    "48x48" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=48",
                                    "24x24" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=24",
                                    "16x16" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=16",
                                    "32x32" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=32"
                                },
                                "displayName" : "rnd_rest_api_account",
                                "active" : true,
                                "timeZone" : "Asia/Seoul"
                            },
                            "body" : "SUCCESS: Integrated in Jenkins build chance_test #10 (See [https://jenkins-rnd.telechips.com:8443/job/chance_test/10/])\n",
                            "updateAuthor" : {
                                "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=rnd_rest_api_account",
                                "name" : "rnd_rest_api_account",
                                "key" : "rndadmin",
                                "emailAddress" : "bluenote212@telechips.com",
                                "avatarUrls" : {
                                    "48x48" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=48",
                                    "24x24" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=24",
                                    "16x16" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=16",
                                    "32x32" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=32"
                                },
                                "displayName" : "rnd_rest_api_account",
                                "active" : true,
                                "timeZone" : "Asia/Seoul"
                            },
                            "created" : "2021-04-14T13:47:49.783+0900",
                            "updated" : "2021-04-14T13:47:49.783+0900"
                        }, 
                        {
                            "self" : "https://tcs.telechips.com:8443/rest/api/2/issue/91867/comment/208741",
                            "id" : "208741",
                            "author" : {
                                "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=rnd_rest_api_account",
                                "name" : "rnd_rest_api_account",
                                "key" : "rndadmin",
                                "emailAddress" : "bluenote212@telechips.com",
                                "avatarUrls" : {
                                    "48x48" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=48",
                                    "24x24" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=24",
                                    "16x16" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=16",
                                    "32x32" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=32"
                                },
                                "displayName" : "rnd_rest_api_account",
                                "active" : true,
                                "timeZone" : "Asia/Seoul"
                            },
                            "body" : "SUCCESS: Integrated in Jenkins build chance_test #11 (See [https://jenkins-rnd.telechips.com:8443/job/chance_test/11/])\n",
                            "updateAuthor" : {
                                "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=rnd_rest_api_account",
                                "name" : "rnd_rest_api_account",
                                "key" : "rndadmin",
                                "emailAddress" : "bluenote212@telechips.com",
                                "avatarUrls" : {
                                    "48x48" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=48",
                                    "24x24" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=24",
                                    "16x16" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=16",
                                    "32x32" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=32"
                                },
                                "displayName" : "rnd_rest_api_account",
                                "active" : true,
                                "timeZone" : "Asia/Seoul"
                            },
                            "created" : "2021-04-14T14:10:43.677+0900",
                            "updated" : "2021-04-14T14:10:43.677+0900"
                        }, 
                        {
                            "self" : "https://tcs.telechips.com:8443/rest/api/2/issue/91867/comment/208743",
                            "id" : "208743",
                            "author" : {
                                "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                                "name" : "B180093",
                                "key" : "b180093",
                                "emailAddress" : "bluenote212@telechips.com",
                                "avatarUrls" : {
                                    "48x48" : "https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                                    "24x24" : "https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                                    "16x16" : "https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                                    "32x32" : "https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                                },
                                "displayName" : "신호찬 (Chance H Shin)",
                                "active" : true,
                                "timeZone" : "Asia/Seoul"
                            },
                            "body" : "build start",
                            "updateAuthor" : {
                                "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                                "name" : "B180093",
                                "key" : "b180093",
                                "emailAddress" : "bluenote212@telechips.com",
                                "avatarUrls" : {
                                    "48x48" : "https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                                    "24x24" : "https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                                    "16x16" : "https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                                    "32x32" : "https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                                },
                                "displayName" : "신호찬 (Chance H Shin)",
                                "active" : true,
                                "timeZone" : "Asia/Seoul"
                            },
                            "created" : "2021-04-14T14:14:40.187+0900",
                            "updated" : "2021-04-14T14:14:40.187+0900"
                        }, 
                        {
                            "self" : "https://tcs.telechips.com:8443/rest/api/2/issue/91867/comment/208744",
                            "id" : "208744",
                            "author" : {
                                "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                                "name" : "B180093",
                                "key" : "b180093",
                                "emailAddress" : "bluenote212@telechips.com",
                                "avatarUrls" : {
                                    "48x48" : "https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                                    "24x24" : "https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                                    "16x16" : "https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                                    "32x32" : "https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                                },
                                "displayName" : "신호찬 (Chance H Shin)",
                                "active" : true,
                                "timeZone" : "Asia/Seoul"
                            },
                            "body" : "build start",
                            "updateAuthor" : {
                                "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=B180093",
                                "name" : "B180093",
                                "key" : "b180093",
                                "emailAddress" : "bluenote212@telechips.com",
                                "avatarUrls" : {
                                    "48x48" : "https://tcs.telechips.com:8443/secure/useravatar?ownerId=b180093&avatarId=10500",
                                    "24x24" : "https://tcs.telechips.com:8443/secure/useravatar?size=small&ownerId=b180093&avatarId=10500",
                                    "16x16" : "https://tcs.telechips.com:8443/secure/useravatar?size=xsmall&ownerId=b180093&avatarId=10500",
                                    "32x32" : "https://tcs.telechips.com:8443/secure/useravatar?size=medium&ownerId=b180093&avatarId=10500"
                                },
                                "displayName" : "신호찬 (Chance H Shin)",
                                "active" : true,
                                "timeZone" : "Asia/Seoul"
                            },
                            "created" : "2021-04-14T14:15:18.177+0900",
                            "updated" : "2021-04-14T14:15:18.177+0900"
                        }, 
                        {
                            "self" : "https://tcs.telechips.com:8443/rest/api/2/issue/91867/comment/208745",
                            "id" : "208745",
                            "author" : {
                                "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=rnd_rest_api_account",
                                "name" : "rnd_rest_api_account",
                                "key" : "rndadmin",
                                "emailAddress" : "bluenote212@telechips.com",
                                "avatarUrls" : {
                                    "48x48" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=48",
                                    "24x24" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=24",
                                    "16x16" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=16",
                                    "32x32" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=32"
                                },
                                "displayName" : "rnd_rest_api_account",
                                "active" : true,
                                "timeZone" : "Asia/Seoul"
                            },
                            "body" : "SUCCESS: Integrated in Jenkins build chance_test #12 (See [https://jenkins-rnd.telechips.com:8443/job/chance_test/12/])\n",
                            "updateAuthor" : {
                                "self" : "https://tcs.telechips.com:8443/rest/api/2/user?username=rnd_rest_api_account",
                                "name" : "rnd_rest_api_account",
                                "key" : "rndadmin",
                                "emailAddress" : "bluenote212@telechips.com",
                                "avatarUrls" : {
                                    "48x48" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=48",
                                    "24x24" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=24",
                                    "16x16" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=16",
                                    "32x32" : "https://www.gravatar.com/avatar/64957cb94e3e6f1833b8e5d6b408cef5?d=mm&s=32"
                                },
                                "displayName" : "rnd_rest_api_account",
                                "active" : true,
                                "timeZone" : "Asia/Seoul"
                            },
                            "created" : "2021-04-14T14:21:40.677+0900",
                            "updated" : "2021-04-14T14:21:40.677+0900"
                        }
                    ],
                    "maxResults" : 6,
                    "total" : 6,
                    "startAt" : 0
                },
                "worklog" : {
                    "startAt" : 0,
                    "maxResults" : 20,
                    "total" : 0,
                    "worklogs" : []
                }
            }
        },
        "changelog" : {
            "id" : "1465196",
            "items" : [ 
                {
                    "field" : "resolution",
                    "fieldtype" : "jira",
                    "from" : "10305",
                    "fromString" : "Done",
                    "to" : null,
                    "toString" : null
                }, 
                {
                    "field" : "status",
                    "fieldtype" : "jira",
                    "from" : "5",
                    "fromString" : "Resolved",
                    "to" : "4",
                    "toString" : "Reopen"
                }
            ]
        }
    },
    "prrameter" : {
        "user_id" : "B180093",
        "user_key" : "b180093"
    },
    "date" : ISODate("2021-04-16T10:53:18.194Z")
}