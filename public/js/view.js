const view = {}

view.setCMSContent = (doc) => { 
    $('#content-container').html(marked(doc));
}


view.setElementContent = (pointer,doc) => {
    $(`${pointer}`).html(doc);
}

view.setRelatedPosts = () => {
    model.loadAllPosts().then(res => {
        console.log(res);
        for (id in res) {
            console.log(res[id]);
            view.createMiniPost(res[id].title,res[id].content);
        }
    })
}

view.createMiniPost = (title, content, truncate=3) => {
    // cut content

    //
    $(`#posts-container`).append(
        `
        <div class="my-4 w-10/12 rounded-md cursor-pointer shadow-lg overflow-hidden hover:shadow-xl transform hover:scale-105 duration-500">
            <div class="p-4 bg-white flex items-start">
                <img class="mr-4 rounded-md" alt="" src="../assets/post-example.png">
                <div class="overflow-y-scroll hide-scroll-bar max-h-40">
                    <h1 class="font-bold text-2xl">${title}</h1>
                    <p class="font-light text-xl">
                        ${content}
                    </p>
                </div>
            </div>
        </div>            
        `
    )
}