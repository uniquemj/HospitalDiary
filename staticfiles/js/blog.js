let saveBtn = document.getElementsByClassName('save-btn')
let draft = document.getElementsByName('draft')

for(let i = 0; i< saveBtn.length; i++){
    saveBtn[i].addEventListener("click",()=>{
        let mark;
        let postId = saveBtn[i].dataset.post
        let action = saveBtn[i].dataset.action
        console.log(postId)
        console.log(action)
        if(draft[i].checked){
            mark = true
        }
        else{
            mark = false
        }
        console.log(mark)
        updateDraftBlog(postId, action, mark)
    })
}

function updateDraftBlog(postId, action, mark){
    url = "/update-draft-blog/"

    $.ajax({
        type: "POST",
        url: url,
        headers:{
            "X-CSRFToken":csrftoken,
        },
        data:{
            postId: postId,
            action: action,
            mark: mark,
        },
        dataType: "json",
        success: function (data) {
            console.log("data: ",data)
            location.reload()
        },
        failure: function(){
            console.log("Blog Update Failed");
        },
    })
}