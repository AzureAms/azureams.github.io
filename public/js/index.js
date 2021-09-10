console.log("hello");

const _init_index = () => {
    // Your web app's Firebase configuration
    var firebaseConfig = {
    };
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    console.log(firebase.app().name);
    // user config
    model.checkUserState().then((user) => {
        console.log(user);
    })
}

$(_init_index);