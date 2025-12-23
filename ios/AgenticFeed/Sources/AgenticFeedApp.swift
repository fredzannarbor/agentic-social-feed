import SwiftUI

/// Agentic Social Feed iOS App
///
/// Version: 1.0.0-allen (David Allen / Getting Things Done - A)
/// Minimum iOS: 18.1 (required for Apple Foundation Models)
///
/// Version naming uses mindful technology thinkers, assigned alphabetically:
/// v1=A (Allen), v2=B (Burkeman), v3=C (Csikszentmihalyi), etc.

@main
struct AgenticFeedApp: App {
    @StateObject private var feedStore = FeedStore()
    @StateObject private var preferences = UserPreferences()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(feedStore)
                .environmentObject(preferences)
        }
    }
}

// MARK: - Version Info

/// Version naming uses mindful technology thinkers alphabetically:
/// - Critics of social media (Haidt, Lanier, Newport, Turkle)
/// - Productivity advocates (Allen, McKeown, Ferriss, Pink)
/// - Flow researchers (Csikszentmihalyi, Robinson)
/// - Focus experts (Kahneman, Ericsson, Duckworth)
struct AppVersion {
    static let major = 1
    static let minor = 0
    static let patch = 0

    static var semver: String {
        "\(major).\(minor).\(patch)"
    }

    /// Thinker info: (codename, full name, work, letter)
    private static let thinkers: [(String, String, String, String)] = [
        ("allen", "David Allen", "Getting Things Done", "A"),           // 1.x
        ("burkeman", "Oliver Burkeman", "Four Thousand Weeks", "B"),    // 2.x
        ("csikszentmihalyi", "Mihaly Csikszentmihalyi", "Flow", "C"),  // 3.x
        ("duckworth", "Angela Duckworth", "Grit", "D"),                 // 4.x
        ("ericsson", "Anders Ericsson", "Peak", "E"),                   // 5.x
        ("ferriss", "Tim Ferriss", "The 4-Hour Workweek", "F"),        // 6.x
        ("grant", "Adam Grant", "Think Again", "G"),                    // 7.x
        ("haidt", "Jonathan Haidt", "The Anxious Generation", "H"),    // 8.x
        ("johnson", "Steven Johnson", "Where Good Ideas Come From", "J"), // 9.x
        ("kahneman", "Daniel Kahneman", "Thinking, Fast and Slow", "K"), // 10.x
        ("lanier", "Jaron Lanier", "Ten Arguments for Deleting Your Social Media", "L"), // 11.x
        ("mckeown", "Greg McKeown", "Essentialism", "M"),              // 12.x
        ("newport", "Cal Newport", "Deep Work", "N"),                   // 13.x
        ("odell", "Jenny Odell", "How to Do Nothing", "O"),            // 14.x
        ("pink", "Daniel Pink", "Drive", "P"),                          // 15.x
        ("robinson", "Ken Robinson", "The Element", "R"),               // 16.x
        ("sinek", "Simon Sinek", "Start with Why", "S"),               // 17.x
        ("turkle", "Sherry Turkle", "Alone Together", "T"),            // 18.x
        ("vanderkam", "Laura Vanderkam", "168 Hours", "V"),            // 19.x
        ("williams", "James Williams", "Stand Out of Our Light", "W"), // 20.x
        ("suzuki", "Shunryu Suzuki", "Zen Mind, Beginner's Mind", "Y"), // 21.x
        ("zomorodi", "Manoush Zomorodi", "Bored and Brilliant", "Z"),  // 22.x
    ]

    static var codename: String {
        let index = major - 1
        return index < thinkers.count ? thinkers[index].0 : "thinker\(major)"
    }

    static var letter: String {
        let index = major - 1
        return index < thinkers.count ? thinkers[index].3 : "?"
    }

    static var full: String {
        "\(semver)-\(codename)"
    }

    static var displayName: String {
        let index = major - 1
        if index < thinkers.count {
            let t = thinkers[index]
            return "\(semver) \"\(t.1)\" (\(t.2))"
        }
        return semver
    }

    static var thinkerInfo: (name: String, work: String)? {
        let index = major - 1
        guard index < thinkers.count else { return nil }
        return (thinkers[index].1, thinkers[index].2)
    }
}
