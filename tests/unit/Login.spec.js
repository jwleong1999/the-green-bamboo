import { mount } from '@vue/test-utils';
import LoginPage from '../../src/views/LoginPage.vue';


// COMMAND TO RUN TEST: npm run test:unit

// -------------------------------------------------------------------------------------------------------------------------------------------------

// -- [TGB-35] VIEW LOGIN PAGE --

describe('View Login Page', () => {
    // Mock data
    const user_data = [
        { Username: "111hotpot", Password: "westlife123", Role: "user" }, // User
    ];
    const producer_data = [
        { Username: "The Macallan Distillery", Password: "macallan!d1st1llery",  Role: "producer"}, // Producer
    ]
    const venue_data = [
        { Username: "GudSht", Password: "datssomegdshit",  Role: "venue" }, // Venue
    ]

    // Mock objects
    const user = { Username: "111hotpot", Password: "westlife123",  Role: "user" }
    const producer = { Username: "The Macallan Distillery", Password: "macallan!d1st1llery",  Role: "producer" }
    const venue = { Username: "GudSht", Password: "datssomegdshit",  Role: "venue" }

    // Mock hashed password
    const hashPassword = jest.fn((id, password) => {
        if (id == "111hotpot" && password == 'westlife123') {
            return '-1531949234';
        }
    });

    // - NO ROLE SELECTED -
    // No role selected for user
    it('[User] No role selected', () => {
        const wrapper = mount(LoginPage, {
            data() {
                return {
                    // Data from mock database
                    users: user_data,
                    producers: producer_data,
                    venues: venue_data,
                    // Test case data
                    role: "", // --> [ERR!] No role selected
                    ID: "111hotpot",
                    password: "westlife123", 
                    // Error handling
                    errors: [],
                };
            },
        });
        // Trigger the checkRole method
        wrapper.vm.checkLogin();
        // Expect an error message indicating that no Role is selected
        expect(wrapper.vm.errors).toContain("No role selected");
    });
    // No role selected for producer
    it('[Producer] No role selected', () => {
        const wrapper = mount(LoginPage, {
            data() {
                return {
                    // Data from mock database
                    users: user_data,
                    producers: producer_data,
                    venues: venue_data,
                    // Test case data
                    role: "", // --> [ERR!] No role selected
                    ID: "The Macallan Distillery",
                    password: "macallan!d1st1llery", 
                    // Error handling
                    errors: [],
                };
            },
        });
        // Trigger the checkRole method
        wrapper.vm.checkLogin();
        // Expect an error message indicating that no Role is selected
        expect(wrapper.vm.errors).toContain("No role selected");
    });
    // No role selected for venue
    it('[Venue] No role selected', () => {
        const wrapper = mount(LoginPage, {
            data() {
                return {
                    // Data from mock database
                    users: user_data,
                    producers: producer_data,
                    venues: venue_data,
                    // Test case data
                    role: "", // --> [ERR!] No role selected
                    ID: "The Macallan Distillery",
                    password: "macallan!d1st1llery", 
                    // Error handling
                    errors: [],
                };
            },
        });
        // Trigger the checkRole method
        wrapper.vm.checkLogin();
        // Expect an error message indicating that no Role is selected
        expect(wrapper.vm.errors).toContain("No role selected");
    });


    // - NO USERNAME ENTERED -
    // No username entered for user
    it('[User] No username entered', () => {
        const wrapper = mount(LoginPage, {
            data() {
                return {
                    // Data from mock database
                    users: user_data,
                    producers: producer_data,
                    venues: venue_data,
                    // Test case data
                    role: user.Role,
                    ID: "", // --> [ERR!] No Username entered
                    password: "westlife123",
                    // Error handling
                    errors: [],
                };
            },
        });
        // Trigger the checkRole method
        wrapper.vm.checkLogin();
        // Trigger the hashPassword method

        // Expect an error message indicating that no Username is entered
        expect(wrapper.vm.errors).toContain("No username entered");
    });
    // No username entered for producer
    it('[Producer] No username entered', () => {
        const wrapper = mount(LoginPage, {
            data() {
                return {
                    // Data from mock database
                    users: user_data,
                    producers: producer_data,
                    venues: venue_data,
                    // Test case data
                    role: producer.Role,
                    ID: "", // --> [ERR!] No Username entered
                    password: "macallan!d1st1llery",
                    // Error handling
                    errors: [],
                };
            },
        });
        // Trigger the checkRole method
        wrapper.vm.checkLogin();
        // Expect an error message indicating that no Username is entered
        expect(wrapper.vm.errors).toContain("No username entered");
    });
    // No username entered for venue
    it('[Venue] No username entered', () => {
        const wrapper = mount(LoginPage, {
            data() {
                return {
                    // Data from mock database
                    users: user_data,
                    producers: producer_data,
                    venues: venue_data,
                    // Test case data
                    role: venue.Role,
                    ID: "", // --> [ERR!] No Username entered
                    password: "datssomegdshit",
                    // Error handling
                    errors: [],
                };
            },
        });
        // Trigger the checkRole method
        wrapper.vm.checkLogin();
        // Expect an error message indicating that no Username is entered
        expect(wrapper.vm.errors).toContain("No username entered");
    });

    // - NO PASSWORD ENTERED -
    // No password entered for user
    it('[User] No password entered', () => {
        const wrapper = mount(LoginPage, {
            data() {
                return {
                    // Data from mock database
                    users: user_data,
                    producers: producer_data,
                    venues: venue_data,
                    // Test case data
                    role: user.Role,
                    ID: "111hotpot",
                    password: "", // --> [ERR!] No password entered
                    // Error handling
                    errors: [],
                };
            },
        });
        // Trigger the checkRole method
        wrapper.vm.checkLogin();
        // Expect an error message indicating that no Password is entered
        expect(wrapper.vm.errors).toContain("No password entered");
    });
    // No password entered for producer
    it('[Producer] No password entered', () => {
        const wrapper = mount(LoginPage, {
            data() {
                return {
                    // Data from mock database
                    users: user_data,
                    producers: producer_data,
                    venues: venue_data,
                    // Test case data
                    role: user.Role,
                    ID: "The Macallan Distillery",
                    password: "", // --> [ERR!] No password entered
                    // Error handling
                    errors: [],
                };
            },
        });
        // Trigger the checkRole method
        wrapper.vm.checkLogin();
        // Expect an error message indicating that no Password is entered
        expect(wrapper.vm.errors).toContain("No password entered");
    });
    // No password entered for venue
    it('[Venue] No password entered', () => {
        const wrapper = mount(LoginPage, {
            data() {
                return {
                    // Data from mock database
                    users: user_data,
                    producers: producer_data,
                    venues: venue_data,
                    // Test case data
                    role: user.Role,
                    ID: "GudSht",
                    Password: "", // --> [ERR!] No password entered
                    // Error handling
                    errors: [],
                };
            },
        });
        // Trigger the checkRole method
        wrapper.vm.checkLogin();
        // Expect an error message indicating that no Password is entered
        expect(wrapper.vm.errors).toContain("No password entered");
    });

    // - INVALID USERNAME -
    // Invalid username for user
    it('[User] Invalid username', () => {
        const wrapper = mount(LoginPage, {
            data() {
                return {
                    // Data from mock database
                    users: user_data,
                    producers: producer_data,
                    venues: venue_data,
                    // Test case data
                    role: user.Role,
                    ID: "loltesting", // --> [ERR!] Invalid username
                    password: "westlife123", 
                    // Error handling
                    errors: [],
                };
            },
        });
        // Trigger the checkRole method
        wrapper.vm.checkLogin();
        // Expect an error message indicating that username is invalid
        expect(wrapper.vm.errors).toContain("Invalid username or password");
    });
    // Invalid username for producer
    it('[Producer] Invalid username', () => {
        const wrapper = mount(LoginPage, {
            data() {
                return {
                    // Data from mock database
                    users: user_data,
                    producers: producer_data,
                    venues: venue_data,
                    // Test case data
                    role: producer.Role,
                    ID: "loltesting", // --> [ERR!] Invalid username
                    password: "macallan!d1st1llery", 
                    // Error handling
                    errors: [],
                };
            },
        });
        // Trigger the checkRole method
        wrapper.vm.checkLogin();
        // Expect an error message indicating that username is invalid
        expect(wrapper.vm.errors).toContain("Invalid username or password");
    });
    // Invalid username for venue
    it('[Venue] Invalid username', () => {
        const wrapper = mount(LoginPage, {
            data() {
                return {
                    // Data from mock database
                    users: user_data,
                    producers: producer_data,
                    venues: venue_data,
                    // Test case data
                    role: producer.Role,
                    ID: "loltesting", // --> [ERR!] Invalid username
                    password: "datssomegdshit", 
                    // Error handling
                    errors: [],
                };
            },
        });
        // Trigger the checkRole method
        wrapper.vm.checkLogin();
        // Expect an error message indicating that username is invalid
        expect(wrapper.vm.errors).toContain("Invalid username or password");
    });

});