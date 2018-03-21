$.ajax({
        type:'get',
        dataType:'json',
        url:'http://127.0.0.1:9000/api/index/?format=json&page=1',
        success:function (data) {

            if (data.code === 200){

                var arr = data.message;

                for (var i=0; i < arr.length; i++){

                    $('#app').append(' <div class="article">\n' +
                        '                <div class="articleHeader">\n' +
                        '                    <h1 class="articleTitle"><a href="'+'http://127.0.0.1:9000/details/'+arr[i]['id']+'">'+arr[i]['title']+'</a></h1>\n' +
                        '                </div>\n' +
                        '                <div class="articleBody clearfix">\n' +
                        '                    <!--缩略图-->\n' +
                        '                    <div class="articleThumb">\n' +
                        '                        <a href="'+'http://127.0.0.1:9000/details/'+arr[i]['id']+'"><img src="'+'http://127.0.0.1:9000/static/'+arr[i]['images']+'" alt="'+arr[i]['title']+'" title="'+arr[i]['title']+'"></a>\n' +
                        '                    </div>\n' +
                        '                    <!--摘要-->\n' +
                        '                    <div class="articleFeed">\n' +
                        '                        <p>'+arr[i]['description']+'</p>\n' +
                        '                    </div>\n' +
                        '                    <!--tags-->\n' +
                        '                    <div class="articleTags">\n' +
                        '                        <ul></ul>\n' +
                        '                    </div>\n' +
                        '                </div>\n' +
                        '                <div class="articleFooter clearfix">\n' +
                        '                    <ul class="articleStatu">\n' +
                        '                        <li><i class="fa fa-calendar"></i>'+arr[i]['date']+'</li>\n' +
                        '                        <li><i class="fa fa-eye"></i>'+arr[i]['count']+'次浏览</li>\n' +
                        '                        <li><a href="#"><i class="fa fa-folder-o"></i></a>\n' +
                        '                            <a href="#" rel="category">'+arr[i]['type']+'</a>\n' +
                        '                        </li>\n' +
                        '                    </ul>\n' +
                        '                    <a href="'+'http://127.0.0.1:9000/details/'+arr[i]['id']+'" class="btn btn-readmore btn-info btn-md">阅读更多</a>\n' +
                        '                </div>\n' +
                        '            </div>\n')
                }
            }
        }

    });

var number = 2;

$('#btn').click(function () {

    $.ajax({
        type:'POST',
        dataType:'json',
        url:'http://127.0.0.1:9000/api/index/?format=json&page='+number,
        success:function (data) {
            if (data.code === 200){
                var arr = data.message;
                for (var i=0; i < arr.length; i++){
                    console.log(arr[i]);
                    $('#app').append(' <div class="article">\n' +
                        '                <div class="articleHeader">\n' +
                        '                    <h1 class="articleTitle"><a href="'+'http://127.0.0.1:9000/details/'+arr[i]['id']+'">'+arr[i]['title']+'</a></h1>\n' +
                        '                </div>\n' +
                        '                <div class="articleBody clearfix">\n' +
                        '                    <!--缩略图-->\n' +
                        '                    <div class="articleThumb">\n' +
                        '                        <a href="'+'http://127.0.0.1:9000/details/'+arr[i]['id']+'"><img src="'+'http://127.0.0.1:9000/static/'+arr[i]['images']+'" alt="'+arr[i]['title']+'" title="'+arr[i]['title']+'"></a>\n' +
                        '                    </div>\n' +
                        '                    <!--摘要-->\n' +
                        '                    <div class="articleFeed">\n' +
                        '                        <p>'+arr[i]['description']+'</p>\n' +
                        '                    </div>\n' +
                        '                    <!--tags-->\n' +
                        '                    <div class="articleTags">\n' +
                        '                        <ul></ul>\n' +
                        '                    </div>\n' +
                        '                </div>\n' +
                        '                <div class="articleFooter clearfix">\n' +
                        '                    <ul class="articleStatu">\n' +
                        '                        <li><i class="fa fa-calendar"></i>'+arr[i]['date']+'</li>\n' +
                        '                        <li><i class="fa fa-eye"></i>'+arr[i]['count']+'次浏览</li>\n' +
                        '                        <li><a href="#"><i class="fa fa-folder-o"></i></a>\n' +
                        '                            <a href="#" rel="category">'+arr[i]['type']+'</a>\n' +
                        '                        </li>\n' +
                        '                    </ul>\n' +
                        '                    <a href="'+'http://127.0.0.1:9000/details/'+arr[i]['id']+'" class="btn btn-readmore btn-info btn-md">阅读更多</a>\n' +
                        '                </div>\n' +
                        '            </div>\n')
                }
            }
        }

    });

    page = ++number;

});


