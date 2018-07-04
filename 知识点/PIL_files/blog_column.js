/**
*@file 专栏改版
*@专栏鼠标移上显示专栏和阅读数
*@author liwz
*@createTime 2016-7-12
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
        },
        //我的专栏与我关注的专栏选项卡
        columnTab: function () {
            var aItem = $(".column_title span"),
                 aItemC = $(".column_box");
            aItem.on("click", function () {
                var index = aItem.index(this);
                $(this).addClass("active_cur").siblings().removeClass("active_cur");
                aItemC.eq(index).show().siblings().hide();
            });
        },
        //从博客列表添加
        multipleAdd: function () {
            var chooseBtn = $("#chooseAdd"),
                oAddPop = $("#addPop"),
                oClose = $("#addClose"),
                aDelete = $(".fa-trash-o");
            chooseBtn.on('click', function () {
                oAddPop.show();
                return false;
            });
            oClose.on('click', function () {
                oAddPop.hide();
                return false;
            });
            aDelete.on('click', function () {
                $(this).parents("li").remove();
                location.reload();
                return false;
            })
        },
        //上下移动位置
        setOrder: function () {
            var setDown = $(".set_down"),
                setUp = $(".set_up");
            setDown.on("click", function () {
                var oLi = $(this).parents("li"),
                    oNextLi = oLi.next();
                if (oNextLi.length != 0)
                    oLi.insertAfter(oNextLi);
                //location.reload();
            });
            setUp.on('click', function () {
                var oLi = $(this).parents("li"),
                    oPrevLi = oLi.prev();
                if (oPrevLi.length != 0)
                    oLi.insertBefore(oPrevLi);
                //location.reload();
            });
        },
        //加关注
        addAttention: function () {
            var oAdd = $("#add_attention");
            var strCon = oAdd.find("em");

            if (strCon.text() == '已关注') {
                oAdd.addClass("grey_focus");
                oAdd.find(".fa").show();
            }

            oAdd.on('click', function () {
                var alias = $(this).attr("alias");
                
                var login_username = getUN();
                if (login_username != '') {
                    if (strCon.text() == '关注') {
                        $.get("/column/ColumnAttention.html?alias=" + alias + "&type=add", function (ret) {
                            if (ret.result == 1) {
                                //$(this).addClass("alreadyAdd");
                                oAdd.addClass("grey_focus");
                                oAdd.find(".fa").show();
                                $("#add_attention em").text('已关注');
                                var count = $(".ba_statistics span").html();
                                $(".ba_statistics span").html(parseInt(count) + 1);
                            }
                            else {
                                alert(ret.content);
                            }
                        });
                    }
                    else if (strCon.text() == '取消关注') {
                        $.get("/column/ColumnAttention.html?alias=" + alias + "&type=del", function (ret) {
                            if (ret.result == 1) {
                                oAdd.find(".fa").hide();
                                oAdd.removeClass("grey_focus");
                                strCon.text('关注');
                                var count = $(".ba_statistics span").html();
                                $(".ba_statistics span").html(parseInt(count) - 1);
                            }
                            else {
                                alert(ret.content);
                            }
                        });


                    }
                }
                else {
                    location.href = "https://passport.csdn.net/account/login?from="+location.href;
                }
            });
            oAdd.hover(function () {
                if (strCon.text() == '已关注') {
                    $(this).find(".fa").hide();
                    strCon.addClass("whiteColor").text("取消关注");
                }
            }, function () {
                if (strCon.text() == '取消关注') {
                    $(this).find(".fa").show();
                    strCon.removeClass("whiteColor").text("已关注");
                }

            })
        },
        //删除专栏文章
        delArticle: function () {

        },
        //管理专栏文章列表
        ArticleList: function () {

        }

    };
    oBlog.columnFn();
    oBlog.backTop();
    oBlog.columnTab();
    oBlog.multipleAdd();
    oBlog.setOrder();
    oBlog.addAttention();
    oBlog.ArticleList();


    $(".choose_img").uploadPreview({ preDiv: 'preview', Img: 'imgPre', width: 1110, height: 170 });

});
/*
     *名称:图片上传本地预览插件 v1.1
     *介绍:基于JQUERY扩展,图片上传预览插件 目前兼容浏览器(IE 谷歌 火狐) 不支持safari
     *插件网站:http://keleyi.com/keleyi/phtml/image/16.htm
     *参数说明: Img:图片ID;Width:预览宽度;Height:预览高度;ImgType:支持文件类型;Callback:选择文件显示图片后回调方法;
     *使用方法:
     <div>
     <img id="ImgPr" width="120" height="120" /></div>
     <input type="file" id="up" />
     把需要进行预览的IMG标签外 套一个DIV 然后给上传控件ID给予uploadPreview事件
     $("#up").uploadPreview({ Img: "ImgPr", Width: 120, Height: 120, ImgType: ["gif", "jpeg", "jpg", "bmp", "png"], Callback: function () { }});
         */


jQuery.fn.extend({
    uploadPreview: function (opts) {
        var _self = this,
                _this = $(this);
        opts = jQuery.extend({
            preDiv: 'preview',
            Img: "imgPre",
            Width: 1110,
            Height: 170,
            ImgType: ["gif", "jpeg", "jpg", "bmp", "png"],
            Callback: function () { }
        }, opts || {});
        _self.getObjectURL = function (file) {
            var url = null;
            if (window.createObjectURL != undefined) {
                url = window.createObjectURL(file)
            } else if (window.URL != undefined) {
                url = window.URL.createObjectURL(file)
            } else if (window.webkitURL != undefined) {
                url = window.webkitURL.createObjectURL(file)
            }
            return url
        };
        _self.show = function () {
            $(".upload_tips").css('color', '#fff');
            $(".change_mask").css('display', 'block');
        }
        _this.change(function () {
            if (this.value) {
                if (!RegExp("\.(" + opts.ImgType.join("|") + ")$", "i").test(this.value.toLowerCase())) {
                    alert("选择文件错误,图片类型必须是" + opts.ImgType.join("，") + "中的一种");
                    this.value = "";
                    return false
                }
                if (/msie/.test(navigator.userAgent.toLowerCase())) {
                    try {
                        //$("#" + opts.Img).attr('src', _self.getObjectURL(this.files[0]))
                        _self.show();
                        $("#" + opts.preDiv).css('backgroundImage', 'url:(' + _self.getObjectURL(this.files[0]) + ')');
                    } catch (e) {
                        var src = "";
                        var obj = $("#" + opts.Img);
                        var div = obj.parent("div")[0];
                        _self.select();
                        if (top != self) {
                            window.parent.document.body.focus()
                        } else {
                            _self.blur();
                        }
                        src = document.selection.createRange().text;
                        document.selection.empty();
                        obj.hide();
                        obj.parent("div").css({
                            'filter': 'progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale)',
                            'width': opts.Width + 'px',
                            'height': opts.Height + 'px'
                        });
                        _self.show();
                        div.filters.item("DXImageTransform.Microsoft.AlphaImageLoader").src = src;
                    }
                } else {
                    _self.show();
                    $("#" + opts.Img).css('display', 'block');
                    $("#" + opts.Img).attr('src', _self.getObjectURL(this.files[0]));
                    //$("#" + opts.preDiv).css('background-image', 'url:('+_self.getObjectURL(this.files[0])+')');
                    //$("#" + opts.preDiv).css('background-image', _self.getObjectURL(this.files[0]));
                }
                opts.Callback();
            }
        })
    }
});


function mycol(e) {
    var b_m = document.cookie.match(new RegExp("(^| )UserName=([^;]*)(;|$)"));
    if (!b_m) {
        e.href = "http://passport.csdn.net/account/login?from=" + encodeURIComponent(e.href);
    }
}

function getUN() {
    var m = document.cookie.match(new RegExp("(^| )UserName=([^;]*)(;|$)"));
    if (m)
        return m[2];
    else
        return '';
}