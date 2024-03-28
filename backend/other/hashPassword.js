function hashPassword(id, password) {
    const combinedString = id.toString() + password;
    let hash = 0;

    for (let i = 0; i < combinedString.length; i++) {
        const char = combinedString.charCodeAt(i);
        hash = (hash << 5) - hash + char;
        hash |= 0; // convert to 32-bit integer
    }

    return hash;
}

let original_id = ["lotusroot518"]
let original_passwords = ["kaihachoo"]

let hashed_passwords = []

for (let i = 0; i < original_id.length; i++) {
    let hashed_password = hashPassword(original_id[i], original_passwords[i])
    hashed_passwords.push(hashed_password)
    console.log(hashed_password)
}