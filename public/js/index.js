console.log("hello");

const _init_index = () => {
    // Your web app's Firebase configuration
    var firebaseConfig = {
        apiKey: "AIzaSyDQNpqrObm5sBZw3Dknis9d-yK--Wk7juM",
        authDomain: "chat-app-45c60.firebaseapp.com",
        databaseURL: "https://chat-app-45c60.firebaseio.com",
        projectId: "chat-app-45c60",
        storageBucket: "chat-app-45c60.appspot.com",
        messagingSenderId: "400495193210",
        appId: "1:400495193210:web:b049d4398169df41161fc3"
    };
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    console.log(firebase.app().name);
    // user config
    // model.checkUserState().then((user) => {
    //     console.log(user);
    // })
    // model.getContent("https://raw.githubusercontent.com/trungnt2910/MemoryModule.NET/master/README.md")
    view.setPost();
    view.setRelatedPosts();
}

$(_init_index);