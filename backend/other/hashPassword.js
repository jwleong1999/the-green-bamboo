export function hashPassword(id, password) {
    const combinedString = id.toString() + password;
    let hash = 0;

    for (let i = 0; i < combinedString.length; i++) {
        const char = combinedString.charCodeAt(i);
        hash = (hash << 5) - hash + char;
        hash |= 0; // convert to 32-bit integer
    }

    return hash;
}

// [VENUES]
// let original_id = ["Orh Gao Taproom", "GudSht", "La Maison Du Whisky", "Auld Alliance", "The Swan Song", "The Single Cask", "Atlas Bar", "Sixteen Ounces", "Junglebird"]
// let original_passwords = ["orhhorsogao", "datssomegdshit", "lalalamaisonnn~~~~", "aaaalliance", "swansongss12312", "only1cask!", "atlasoratasbar??", "16oz!", "chirpingaway"]

// [PRODUCERS]
// let original_id = ["Little Creatures", "Choya", "Archie Rose Distilling", "Nagahama Distillery", "Fuji Distillery", "Dassai Brewery", "Hampden Estate Rum", "Lion City Meadery", "Orion", "Taiwan Beer", "Glenfiddich Distillery", "Engkanto Brewery", "Alive Brewing", "Seoul Jangsoo Co. Ltd"]
// let original_passwords = ["Littl123", "Choya123", "Archi123", "Nagah123", "Fuji 123", "Dassa123", "Hampd123", "Lion 123", "Orion123", "Taiwa123", "Glenf123", "Engka123", "Alive123", "Seoul123"]

// let hashed_passwords = []

// for (let i = 0; i < original_id.length; i++) {
//     let hashed_password = hashPassword(original_id[i], original_passwords[i])
//     hashed_passwords.push(hashed_password)
//     console.log(hashed_password)
// }