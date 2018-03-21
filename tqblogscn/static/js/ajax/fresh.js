
$.ajax({
   type:'get',
   dateType:'json',
   url:'http://127.0.0.1:9000/api/fresh/?format=json&page=1',
   success:function (data) {
       if(data.code === 200){

           var arr = data.message;

           for (var i=0; i<arr.length;i++){

                   $('#app').append('                <div class="article" id="'+arr[i]['id']+'">\n' +
                   '\t\t\t\t\t<div class="articleHeader">\n' +
                   '\t\t\t\t\t\t<h1 class="articleTitle"><a href="'+arr[i]['url']+'">'+arr[i]['title']+'</a></h1>\n' +
                   '\t\t\t\t\t\t<span class="cate-Div">\n' +
                   '\t\t\t\t\t\t\t<i class="fa fa-map-marker"></i>'+arr[i]['views']+'</span>\n' +
                   '\t\t\t\t\t</div>\n' +
                   '\t\t\t\t\t<div class="articleFooter clearfix">\n' +
                   '\t\t\t\t\t\t<ul class="articleStatu">\n' +
                   '\t\t\t\t\t\t\t<li><i class="fa fa-calendar"></i>'+arr[i]['create_time']+'</li>\n' +
                   '\t\t\t\t\t\t\t<li><a href="#"><i class="fa fa-folder-o"></i>\n' +
                   '\t\t\t\t\t\t\t</a><a href="#" rel="category">'+arr[i]['category']+'</a></li>\n' +
                   '\t\t\t\t\t\t</ul>\n' +
                   '\t\t\t\t\t\t<a href="'+arr[i]['url']+'" class="btn btn-readmore btn-info btn-md">上车</a>\n' +
                   '\t\t\t\t\t</div>\n' +
                   '\t\t\t\t</div>\n');
                }

            }
        }
    });


var number = 2;

 $('#btn').click(function () {
        $.ajax({
               type:'post',
               dateType:'json',
               url:'http://127.0.0.1:9000/api/fresh/?format=json&page='+number,
               success:function (data) {
                   if(data.code === 200){
                       var arr = data.message;
                       for (var i=0; i<arr.length;i++){

                           $('#app').append('                <div class="article" id="article">\n' +
                               '\t\t\t\t\t<div class="articleHeader">\n' +
                               '\t\t\t\t\t\t<h1 class="articleTitle"><a href="\'+arr[i][\'url\']+\'">'+arr[i]['title']+'</a></h1>\n' +
                               '\t\t\t\t\t\t<span class="cate-Div">\n' +
                               '\t\t\t\t\t\t\t<i class="fa fa-map-marker"></i>'+arr[i]['views']+'</span>\n' +
                               '\t\t\t\t\t</div>\n' +
                               '\t\t\t\t\t<div class="articleFooter clearfix">\n' +
                               '\t\t\t\t\t\t<ul class="articleStatu">\n' +
                               '\t\t\t\t\t\t\t<li><i class="fa fa-calendar"></i>'+arr[i]['create_time']+'</li>\n' +
                               '\t\t\t\t\t\t\t<li><a href="#"><i class="fa fa-folder-o"></i>\n' +
                               '\t\t\t\t\t\t\t</a><a href="#" rel="category">'+arr[i]['category']+'</a></li>\n' +
                               '\t\t\t\t\t\t</ul>\n' +
                               '\t\t\t\t\t\t<a href="'+arr[i]['url']+'" class="btn btn-readmore btn-info btn-md">上车</a>\n' +
                               '\t\t\t\t\t</div>\n' +
                               '\t\t\t\t</div>\n');

                        }
                    }
                }
            });

        page = number++;

    });

