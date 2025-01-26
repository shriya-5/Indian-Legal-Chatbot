
import numpy as np

knowledge_graph = {
    "Cyber Crime": {
        "Types": ["phishing", "cyber stalking", "cyber defamation", "cyber hacking", "cyber harassment", "software piracy"],
    },
    "phishing": {
        "defined as": "Phishing attacks are fraudulent emails, text messages, phone calls or web sites designed to trick users into downloading malware, sharing sensitive information or personal data",
        "law_defined": [
            "Section 43: If any person without the permission of the owner of the computer, computer system, computer network; accesses, downloads, introduces, disrupts, denies, or provides any assistance to other people can be held liable under this section.",
            "Section 66: This section provides for punishment if the accounts of a victim are compromised by the phisher, who does any act mentioned in Section 43 of the IT act, shall be imprisoned for a term which may exceed up to three years or with a fine which may exceed up to five lakh rupees or both.",
            "Section 66C: This provision prohibits the use of electronic signatures, passwords, and any other feature which is a unique identification of a person. Phishers disguise and portray themselves as the true owners of the accounts and perform fraudulent acts. It is related to Identity Theft by phisher.",
            "Section 66D: The provision provides punishment for cheating by personating using communication devices or computer sources. Fraudsters use URLs that contain the link for a fake website of banks and organizations and personate themselves as the bank or the financial institution."
        ],
        "reporting_steps": "If you suspect a phishing attempt, immediately report it to the concerned authorities or the organization.To report phishing attempts, spoofing, or to report that you've been a victim, visit the Internet Crime Complaint Center (IC3) to file a complaint.To report an online scam on the portal, follow these steps: Open your web browser and navigate to the portal's webpage at https://cybercrime.gov.in. On the homepage, click on 'File a complaint'. Read and accept the terms and conditions on the next page. Click on the 'Report other cybercrime' button. Select the 'citizen login' option and enter your details, including name, email, and phone number. Enter the OTP sent to your registered phone number, fill in the captcha, and click on the submit button. On the next page, provide details about the cybercrime you wish to report. The form is divided into four sections: General Information, Victim Information, Cybercrime Information, and Preview. Fill in all relevant details in each section. After reviewing the information, click on the 'Submit' button. You will be directed to an incident details page. Here, provide details and supporting evidence of the crime, such as screenshots or files. Once you've entered the details, click on 'Save and Next'. The next page requires information about the alleged suspect if available. Fill in the details if you have any information about the suspect. Verify the information and click on the 'Submit' button. You will receive a confirmation message that your complaint has been registered, along with an email containing the complaint ID and other related details.",
    },
    "cyber harassment": {
        "defined as": "Cyber harassment is harassment that takes place over digital devices like cell phones, computers, and tablets. Cyber harassment can occur through SMS, Text, and apps, or online in social media, forums, or gaming where people can view, participate in, or share content. Cyber harassment includes sending, posting, or sharing negative, harmful, false, or mean content about someone else. It can include sharing personal or private information about someone else causing embarrassment or humiliation.",
        "law_defined": [
            "Section 507 IPC: According to the clause, if someone gets criminal intimidation by anonymous communication, the person who threatened, must be punished with either type of jail for a duration that may last up to two years. Bullying and cyberbullying are crimes. This section addresses bullying because the word anonymous is used.",
            "Section 66E:  A section of the IT Act outlines penalties for privacy violations. According to the clause, whoever willfully violates another person’s privacy by sending, photographing, or publishing their private images would be penalized with either a term of imprisonment up to three years or a fine up to three lakhs."
        ],
        "reporting_steps": "Identify and block the bully's phone number to prevent him/her from sending messages. Save all the chats, posts, and emails sent by the bully to be used as evidence. Report the bully's phone number/account details to the service providers - all social networking platforms have this facility."
    },
    "cyber hacking": {
        "defined as": "Cyber hacking, also known as cyber attacking, is the practice of intentionally exploiting weaknesses in an organization's computer systems. Cyber hacking can be used for purposes such as compromising or stealing data, disrupting communication or procedures, or to satisfy other harmful objectives.",
        "law_defined": [
            "Section 66B: Whoever dishonestly receive or retains any stolen computer resource or communication device knowing or having reason to believe the same to be stolen computer resource or communication device, shall be punished with imprisonment of either description for a term which may extend to three years or with fine which may extend to rupees one lakh or with both."
        ],
        "reporting_steps": "Identify and block the bully's phone number to prevent him/her from sending messages. Save all the chats, posts, and emails sent by the bully to be used as evidence. Report the bully's phone number/account details to the service providers - all social networking platforms have this facility."
    },
    "software piracy": {
        "defined as": "Software piracy is the illegal use or copy of paid software with violation of copyrights or license restrictions. An example of software piracy is when you download a fresh non-activated copy of Windows and use what is known as “Cracks” to obtain a valid license for Windows activation. This is considered software piracy. Not only software can be pirated but also music, movies, or pictures.",
        "law_defined": [
            "Section 51: Copyright in a work shall be deemed to be infringed— when any person, without a licence granted by the owner of the copyright or the Registrar of Copyrights under this Act or in contravention of the conditions of a licence so granted or of any condition imposed by a competent authority under this Act—does anything, the exclusive right to do which is by this Act conferred upon the owner of the copyright, or permits for profit any place to be used for the communication of the work to the public where such communication constitutes an infringement of the copyright in the work unless he was not aware and had no reasonable ground for believing that such communication to the public would be an infringement of copyright.",
            "Section 65B: Any person, who knowingly,—removes or alters any rights management information without authority, or distributes, imports for distribution, broadcasts or communicates to the public, without authority, copies of any work, or performance knowing that electronic rights management information has been removed or altered without authority, shall be punishable with imprisonment which may extend to two years and shall also be liable to fine:",
            "Section 63B: Knowing use of infringing copy of computer programme to be an offence. Any person who knowingly makes use on a computer of an infringing copy of a computer programme shall be punishable with imprisonment for a term which shall not be less than seven days but which may extend to three years and with fine which shall not be less than fifty thousand rupees but which may extend to two lakh rupees: Provided that where the computer programme has not been used for gain or in the course of trade or business, the court may, for adequate and special reasons to be mentioned in the judgment, not impose any sentence of imprisonment and may impose a fine which may extend to fifty thousand rupees."
        ],
        "reporting_steps": "To report online piracy- One can dial the 10-digit number 1600-334455 from any part of the country free of cost to report a case of companies using pirated software."
    },
    "cyber defamation": {
        "defined as": "Cyber defamation, also known as online defamation, is the act of making false or derogatory statements about someone over the internet. This can include statements made on social media, forums, blogs, or any other online platform.",
        "law_defined": [
            "Section 500: Punishment for defamation—Whoever defames another shall be punished with simple imprisonment for a term which may extend to two years, or with fine, or with both.",
            "Section 499: Whoever, by words either spoken or intended to be read, or by signs or by visible representations, makes or publishes any imputation concerning any person intending to harm, or knowing or having reason to believe that such imputation will harm, the reputation of such person, is said, except in the cases hereinafter expected, to defame that person."
        ],
        "reporting_steps": "To report online piracy- One can dial the 10-digit number 1600-334455 from any part of the country free of cost to report a case of companies using pirated software."
    },
}