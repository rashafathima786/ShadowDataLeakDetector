from utils import calculate_behavior_score

def main():
    print("=== Shadow Data Leak Detector ===")

    password_reuse = int(input("Password reused? (1 = Yes, 0 = No): "))
    public_wifi = int(input("Uses public Wi-Fi frequently? (1 = Yes, 0 = No): "))
    two_factor_enabled = int(input("2FA enabled? (1 = Yes, 0 = No): "))
    password_change_frequency = int(input("Password change frequency (months): "))
    platform_count = int(input("Number of platforms used: "))

    score = calculate_behavior_score(
        password_reuse,
        public_wifi,
        two_factor_enabled,
        password_change_frequency,
        platform_count
    )

    print("\nFinal Risk Score:", score)

    if score >= 70:
        print("⚠️ High Risk – Immediate action recommended")
    elif score >= 40:
        print("⚠️ Medium Risk – Improve security habits")
    else:
        print("✅ Low Risk – Good security practices")

# THIS LINE IS CRITICAL
if __name__ == "__main__":
    main()
