/**
 * Created with PyCharm.
 * User: wangjian2254
 * Date: 13-3-6
 * Time: 上午2:17
 * To change this template use File | Settings | File Templates.
 */
function getReplay(id,divid)
    {
        if($('#'+divid).css('display')=='block'){
            $('#'+divid).hide();
            return;
        }
        if($('#'+divid).css('display')=='none'){
                    $('#'+divid).show();
                   if($('#'+divid).html()!=''){
                       return;
                   }
         }
        var commentlistdata;
        $.ajax({type: "GET",
            url: "/joke/commentList",
            data:{jokeid:id},
            dataType:'json',
            async: true,
            success: function(data){
                var datamap=new Object();
                var dataarr=new Array();
                var dataobj;
                var dataobj2;
                for(var i=0;i<data.length;i++){
                    dataobj=data[i];
                    if(dataobj['fatherid']){
                        if(!datamap[dataobj['fatherid']]['children']){
                            datamap[dataobj['fatherid']]['children']=new Array();
                        }
                        datamap[dataobj['fatherid']]['children'].push(dataobj);
                    }else{
                        dataarr.push(dataobj);
                    }
                    datamap[dataobj['id']]=dataobj;
                }
               var commenthtml0='<div class="commentlist"><table  border="0" cellpadding="0" cellspacing="0" ><tr class="top"><td rowspan="4" width="60px" valign="bottom"><img src="/static/img/default/face/face';
               var commenthtml1='.gif"  /></td><td class="commenttl"></td><td  class="commentt"></td><td class="commenttr"></td></tr><tr><td class="commentl"></td><td class="commentc">';
               var commenthtml2='</td><td class="commentr"></td></tr><tr class="bottom"><td class="commentbl"></td><td class="commentb"></td><td class="commentbr"></td></tr><tr><td colspan="2" height="25"></td></tr></table>';
               var commenthtml3='</div>';

               var replayhtml0='<div class="replaylist"><table  border="0" cellpadding="0" cellspacing="0" align="right"><tr class="top"><td class="commentrtl"></td><td  class="commentrt"></td><td class="commentrtr"></td><td rowspan="4" width="60px" valign="bottom"><img src="/static/img/default/face/face';
               var replayhtml1= '.gif"  /></tr><tr><td class="commentrl"></td><td class="commentrc">';
               var replayhtml2='</td><td class="commentrr"></td></tr><tr class="bottom"><td class="commentrbl"></td><td class="commentrb"></td><td class="commentrbr"></td></tr></table></div>';
                for(var j=0;j<dataarr.length;j++){
                   dataobj=dataarr[j];
                    var replayhtml=commenthtml0+dataobj['face']+commenthtml1+'<span id="'+dataobj['id']+'txt">'+dataobj['username']+':<br/>'+dataobj['createDate']+'<br/>'+dataobj['content']+'</span>'+'<div class="reply">'+commenthtml2;
                    //var replayhtml=commenthtml0+dataobj['face']+commenthtml1+'<span id="'+dataobj['id']+'txt">'+dataobj['username']+':<br/>'+dataobj['createDate']+'<br/>'+dataobj['content']+'</span>'+'<div class="reply"><a href="#replay" class="replytool" onclick="replay(\''+dataobj['id']+'\')">回复</a>'+commenthtml2;
                    if(dataobj['children']){
                        for(var k=0;k<dataobj['children'].length;k++){
                            dataobj2=dataobj['children'][k];
                            replayhtml+=replayhtml0+dataobj2['face'];
                            replayhtml+=replayhtml1+'<span id="'+dataobj2['id']+'txt">'+dataobj2['username']+':<br/>'+dataobj2['createDate']+'<br/>'+dataobj2['content']+'</span>';
                            replayhtml+=replayhtml2;
                        }
                    }
                    replayhtml+=commenthtml3;
                    $('#'+divid).append(replayhtml);
               }
            }
        });
    };
function getCommentNum(id,divid){
    $.ajax({type: "POST",
                       url: "/replay/"+id,
                       data:{jokeid:id},
                       dataType:'json',
                       async: true,
                       success: function(data){
                              if(data.success){
                                  //$('#showNumFont').html(data.showNum);
                                  $('#'+divid).html("("+data.replaynum+")");
                              }
                       }

                   })
}