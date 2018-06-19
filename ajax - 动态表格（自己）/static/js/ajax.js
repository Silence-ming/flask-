 function ajax(obj){
        if(!obj){
            console.error("请输入参数")
            return
        }
        if(typeof obj!="object"){
            console.error("请输入正确格式")
            return
        }
        if(!obj.url){
            console.error("请输入地址")
            return
        }
        var url=obj.url; //地址
        var type=obj.type || "get";  //请求方式，当type不传时，默认为“get”
        var async=obj.async===false?false:true; //异步机制
        var datatype=obj.datatype || "string";  //当datatype不传时，返回string
        if(obj.data){
            if(typeof obj.data == "object"){  //当传入的data格式为json格式时，拼接字符串
                var str="";
                for(var i in obj.data){
                    str+=i+"="+obj.data[i]+"&"
                }
                var data="?"+str.slice(0,-1);
            }else{
                var data="?"+obj.data;   //当传入的data格式为字符串时，返回它本身
            }
        }else{
            return
        }
        var xmlobj=new XMLHttpRequest();
        //实时监测请求的数据，返回需要的数据类型
        xmlobj.onload=function(){
            if(datatype=="string"){
                obj.success(xmlobj.responseText)
            }
            if(datatype=="json"){
                obj.success(JSON.parse(xmlobj.response))
            }
            if(datatype=="text"){
                obj.success(xmlobj.responseText)
            }
        }
        if(type=="get"){  //如果请求方式为get
            xmlobj.open(type,url+data,async)
            xmlobj.send()
        }else if(type=="post"){  //如果请求方式为post
            xmlobj.open(type,url,async)
            xmlobj.setRequestHeader("content-type","application/x-www-form-urlencoded")
            xmlobj.send(data.slice(1))
        }
    }
    // ajax({
    //     url:"/ajax",
    //     type:"get",
    //     async:false,
    //     datatype:"text",
    //    data:{name:"lisi"},
    //     success:function(a){
    //         console.log( a)
    //     }
    // })