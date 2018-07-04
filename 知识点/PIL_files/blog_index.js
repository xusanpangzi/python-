/**
*@file 博客改版
*@专栏鼠标移上显示专栏和阅读数
*@author liwz
*@createTime 2016-5-12
*/

$(function () {
    var oBlog = {
        //专栏模块鼠标移上显示专栏和阅读数
        columnFn: function () {
            var aColumn = $(".column_list_link");
            aColumn.hover(function () {
                $(this).find(".column_list_b").show().end().siblings().find(".column_list_b").hide();
            }, function () {
                $(this).find(".column_list_b").hide().end().siblings().find(".column_list_b").show();
            });
        },
        //热文排行榜选项卡
        hotList: function () {
            var aList = $("#List span"),
                oListC = $("#hot_wrap");
            //var aData = [['独立网站支付宝接口0','独立网站支付宝接口','独立网站支付宝接口','独立网站支付宝接口','独立网站支付宝接口'],['独立网站支付宝接口1','独立网站支付宝接口1','独立网站支付宝接口','独立网站支付宝接口','独立网站支付宝接口'],['独立网站支付宝接口2','独立网站支付宝接口2','独立网站支付宝接口','独立网站支付宝接口','独立网站支付宝接口']]

            aList.on("click", function () {
                var days = $(this).html();
                if (days == "日榜") {
                    days = 1;
                }
                else if (days == "周榜") {
                    days = 8;
                }
                else {
                    days = 31;
                }
                $(this).addClass('list_cur').siblings().removeClass('list_cur');  
                
                
                $.get("/GetHotArticles.html?days=" + days, function (data) {                   
                    
                    var oLi = '';
                    oListC.html('');
                    $.each(data, function (index, item) {
                        oLi += '<li><a href="http://blog.csdn.net/' + item.UserName + '/article/details/' + item.ArticleId + '"><i class="fa fa-caret-right"></i><span>' + item.Title + '</span></a></li>';
                    });
                    oListC.append(oLi);                  
                });
                                     
            });
        },
        //加载更多
        loadMore: function () {
            
            $(".loadMore").click(function () {
                $(".loadMore_icon").show().addClass("circle_move");
                $(".loadMore").hide();
                $("#listBot2").show();
                $(".loadMore_icon").remove();
                $(".page_nav").show();
            });

            var num = 0;
            $(window).scroll(function()
            {
                var srcollTop = $(this).scrollTop();
                var scrollHeight = $(document).height();
                var windowH = $(this).height();
                if(srcollTop + windowH +300 >= scrollHeight)
                {
                    if(num == 0)
                    {   
                        var listbot2 = $("#listBot2 dl");
                        if (listbot2.length > 0) {
                            setTimeout(function () {
                                $(".loadMore_icon").show().addClass("circle_move");
                                $(".loadMore").hide();
                                $("#listBot2").show();
                                $(".loadMore_icon").remove();
                                $(".page_nav").show();
                            }, 1000);
                        }
                        else {
                            $(".loadMore").html("没有更多");
                        }

                        $(window).unbind('scroll');
                    }
                }
            })
            
        },
        //返回顶部
        backTop: function () {
            var oBackTop = $('#backTop');
            oBackTop.click(function () {
                $("body,html").animate({ scrollTop: 0 }, 500);
            });

            var backToFun = function () {
                var scrollTop = $(document).scrollTop();
                var winh = $(window).height();
                (scrollTop > 0) ? oBackTop.show() : oBackTop.hide();
                //IE6下的定位
                if (!window.XMLHttpRequest) {
                    oBackTop.css("top", scrollTop + winh - 86);
                }
            }
            $(window).on('scroll', backToFun);
            backToFun();
        }
    };
    oBlog.columnFn();
    oBlog.hotList();
    oBlog.loadMore();
    oBlog.backTop();

});


