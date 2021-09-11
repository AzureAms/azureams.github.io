const model = {}

model.currentUser = null

model.checkUserState = async (redirect=true) => {
    return firebase.auth().onAuthStateChanged((user) => {
        if (user) {
            if (user.emailVerified) {
                model.currentUser = user;
                console.log("bruhh")
            } else {
                alert("PLEASE VERIFY YOUR EMAIL !!!")
                model.currentUser = user;
                console.log(user)
            }
        } else {
          console.log("anonymous")
        }
    });
}

model.login = async (email,pwd) => {
    await firebase.auth().signInWithEmailAndPassword(email,pwd);
    return firebase.auth().currentUser;
}

model.logout = () => {
    firebase.auth().signOut().then(() => {
      console.log("LOG OUT !!!");
    }).catch((err) => {
      console.log(err);
    });
  }

model.createPost = async (post, tags, user) => {
    ownerInfo = null;
    if (user) ownerInfo = user;
    if (model.currentUser) ownerInfo = model.getUserInfo();
    if (!owner) throw "Error";
    return await firebase.firestore().collection("posts").add({
        owner: ownerInfo,
        content: post,
        tags: tags,
        uploadTime : new Date(),
    })
}

model.getUserInfo = async (uid,current=true) => {
    if (current) return firebase.firestore().collection('users').doc(firebase.auth().currentUser.uid).get()
    // else return firebase.firestore().collection('users').doc(firebase.auth().currentUser.uid).get();
}

model.loadPostsbyTags = async (tagName) => {
    return firebase.firestore().collection('posts').where("tags","array-contains", tagName)
    .then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
            console.log(doc.id, " => ", doc.data())
        }) 
    })
}

model.loadAllPosts = async () => {
    var querySnapshot = await firebase.firestore().collection('posts').get()
    var res = {};
    querySnapshot.forEach((doc) => {
        console.log(doc.id, " => ", doc.data())
        res[doc.id] = doc.data();
    })
    return res;
}

model.loadPostbyID = (id) => {
    return firebase.firestore().collection('posts').doc(id).get()
    .then(res => res.data())
}


model.getContent = (url) => {
    return fetch(url).then(res => res.text())
}


