
$.ajax({
   type:'get',
   dateType:'json',
   url:'http://127.0.0.1:9000/api/collection/?format=json&page=1',
   success:function (data) {
       if(data.code === 200){

           var arr = data.message;

           for (var i=0; i<arr.length;i++){

                   $('#app').append('            <div class="article">\n' +
                       '                <div class="articleHeader">\n' +
                       '                    <h1 class="articleTitle"><a href="'+arr[i]['url']+'">'+arr[i]['title']+'（'+arr[i]['url']+'） </a></h1>\n' +
                       '                </div>\n' +
                       '                <div class="articleBody clearfix">\n' +
                       '                    <!--缩略图-->\n' +
                       '                    <div class="articleThumb">\n' +
                       '                        <a href="'+arr[i]['url']+'"><img src="'+'http://127.0.0.1:9000/static/'+arr[i]['images']+'" alt="'+arr[i]['title']+'" title="'+arr[i]['title']+'"></a>\n' +
                       '                    </div>\n' +
                       '                    <!--摘要-->\n' +
                       '                    <div class="articleFeed">\n' +
                       '                        <p>'+arr[i]['abstract']+'</p>\n' +
                       '                    </div>\n' +
                       '                    <!--tags-->\n' +
                       '                    <div class="articleTags">\n' +
                       '                        <ul></ul>\n' +
                       '                    </div>\n' +
                       '                </div>\n' +
                       '                <div class="articleFooter clearfix">\n' +
                       '                    <ul class="articleStatu">\n' +
                       '                        <li><i class="fa fa-calendar"></i>'+arr[i]['create_time']+'</li>\n' +
                       '                        <li><a href="#"><i class="fa fa-folder-o"></i></a>\n' +
                       '                            <a href="#" rel="category">博客收录</a>\n' +
                       '                        </li>\n' +
                       '                    </ul>\n' +
                       '                    <a href="'+arr[i]['url']+'" class="btn btn-readmore btn-info btn-md">直通车</a>\n' +
                       '                </div>\n' +
                       '            </div>\n')

                }

            }
        }
    });


var number = 2;

 $('#btn').click(function () {
        $.ajax({
               type:'post',
               dateType:'json',
               url:'http://127.0.0.1:9000/api/collection/?format=json&page='+number,
               success:function (data) {
                   if(data.code === 200){
                       var arr = data.message;
                       for (var i=0; i<arr.length;i++){

                           $('#app').append('            <div class="article">\n' +
                       '                <div class="articleHeader">\n' +
                       '                    <h1 class="articleTitle"><a href="'+arr[i]['url']+'">'+arr[i]['title']+'（'+arr[i]['url']+'） </a></h1>\n' +
                       '                </div>\n' +
                       '                <div class="articleBody clearfix">\n' +
                       '                    <!--缩略图-->\n' +
                       '                    <div class="articleThumb">\n' +
                       '                        <a href="'+arr[i]['url']+'"><img src="'+arr[i]['images']+'" alt="'+arr[i]['title']+'" title="'+arr[i]['title']+'"></a>\n' +
                       '                    </div>\n' +
                       '                    <!--摘要-->\n' +
                       '                    <div class="articleFeed">\n' +
                       '                        <p>'+arr[i]['abstract']+'</p>\n' +
                       '                    </div>\n' +
                       '                    <!--tags-->\n' +
                       '                    <div class="articleTags">\n' +
                       '                        <ul></ul>\n' +
                       '                    </div>\n' +
                       '                </div>\n' +
                       '                <div class="articleFooter clearfix">\n' +
                       '                    <ul class="articleStatu">\n' +
                       '                        <li><i class="fa fa-calendar"></i>'+arr[i]['create_time']+'</li>\n' +
                       '                        <li><a href="#"><i class="fa fa-folder-o"></i></a>\n' +
                       '                            <a href="#" rel="category">博客收录</a>\n' +
                       '                        </li>\n' +
                       '                    </ul>\n' +
                       '                    <a href="'+arr[i]['url']+'" class="btn btn-readmore btn-info btn-md">直通车</a>\n' +
                       '                </div>\n' +
                       '            </div>\n');

                        }
                    }
                }
            });

        page = number++;

    });

