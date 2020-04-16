import Mock from 'mockjs'

Mock.mock('/getnewslist',{
    'list|5':[
        {
            url:'@url',
            title:'@ctitle(5,20)'
        }
    ]
})