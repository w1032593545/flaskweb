import Mock from 'mockjs'

Mock.mock(/getNewsList/,{
    'list|5':[
        {
            'url':'@url',
            'title':'@ctitle(5,20)'
        }
    ]
})

Mock.mock(/getProductList/,{
    'pc': {
        'last':true,
        'title': "@ctitle(4)",
        'list': [
          {
            'title': "@ctitle(5)",
            'url': "@url",
            'hot':"@boolean"
          },
          {
            'title': "@ctitle(5)",
            'url': "@url",
            'hot':"@boolean"
          },
          {
            'title': "@ctitle(5)",
            'url': "@url",
            'hot':"@boolean"
          },
          {
            'title': "@ctitle(5)",
            'url': "@url",
            'hot':"@boolean"
          },
        ]
      },
      'app': {
        'title': "@ctitle(4)",
        'list': [
            {
                'title': "@ctitle(5)",
                'url': "@url",
                'hot':"@boolean"
            },
              {
                'title': "@ctitle(5)",
                'url': "@url",
                'hot':"@boolean"
              },
              {
                'title': "@ctitle(5)",
                'url': "@url",
                'hot':"@boolean"
              },
              {
                'title': "@ctitle(5)",
                'url': "@url",
                'hot':"@boolean"
              },
        ]
      }
})

Mock.mock(/getBoarderList/,[
    {
        title:"@ctitle(4)",
        description:"@ctitle(8,12)",
        saleout:'@boolean'
    },
    {
        title:"@ctitle(4)",
        description:"@ctitle(8,12)",
        saleout:'@boolean'
    },
    {
        title:"@ctitle(4)",
        description:"@ctitle(8,12)",
        saleout:'@boolean'
    },
    {
        title:"@ctitle(4)",
        description:"@ctitle(8,12)",
        saleout:'@boolean'
    },
])

export default Mock