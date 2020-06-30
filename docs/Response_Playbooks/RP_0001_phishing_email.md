| Titre             | E-mail malveillant                                                                                                      |
|:-----------------:|:-----------------------------------------------------------------------------------------------------------------|
| **ID**            | RP0001            |
| **Description**   | Playbook de réponse pour le cas d'un courrier électronique malveillant   |
| **Auteur**        | @atc_project        |
| **Date de création** | 31.01.2019 |
| **Gravité**      | M      |
| **TLP**           | AMBER           |
| **PAP**           | WHITE           |
| **ATT&amp;CK Tactic**  |<ul><li>[TA0001: Initial Access](https://attack.mitre.org/tactics/TA0001)</li></ul>|
| **ATT&amp;CK Technique**  |<ul><li>[T1193: Spearphishing Attachment](https://attack.mitre.org/tactics/T1193)</li><li>[T1192: Spearphishing Link](https://attack.mitre.org/tactics/T1192)</li></ul>|
| **Tags**          | <ul><li>phishing</li></ul> |
| **Preparation**  |<ul><li>[RA1001: S'exercer](../Response_Actions/RA_1001_practice.md)</li><li>[RA1002: Suivre des formations](../Response_Actions/RA_1002_take_trainings.md)</li><li>[RA1004: Obliger le personnel à signaler une activité suspecte](../Response_Actions/RA_1004_make_personnel_report_suspicious_activity.md)</li><li>[RA1003: Sensibiliser le personnel](../Response_Actions/RA_1003_raise_personnel_awareness.md)</li><li>[RA1101: Accéder aux journaux de flux du réseau externe](../Response_Actions/RA_1101_access_external_network_flow_logs.md)</li><li>[RA1104: Accéder aux journaux HTTP externes](../Response_Actions/RA_1104_access_external_http_logs.md)</li><li>[RA1106: Accéder aux journaux DNS externes](../Response_Actions/RA_1106_access_external_dns_logs.md)</li><li>[RA1111: Obtenir la possibilité de bloquer l'adresse IP externe](../Response_Actions/RA_1111_get_ability_to_block_external_ip_address.md)</li><li>[RA1113: Obtenir la possibilité de bloquer un domaine externe](../Response_Actions/RA_1113_get_ability_to_block_external_domain.md)</li><li>[RA1115: Obtenir la possibilité de bloquer l'url externe](../Response_Actions/RA_1115_get_ability_to_block_external_url.md)</li><li>[RA1201: Obtenir la possibilité de répertorier les e-mails ouverts des utilisateurs](../Response_Actions/RA_1201_get_ability_to_list_users_opened_email_message.md)</li><li>[RA1202: Obtenir la possibilité de répertorier les destinataires des e-mails](../Response_Actions/RA_1202_get_ability_to_list_email_message_receivers.md)</li><li>[RA1203: Obtenir la possibilité de bloquer le domaine de messagerie](../Response_Actions/RA_1203_get_ability_to_block_email_domain.md)</li><li>[RA1204: Obtenir la possibilité de bloquer l'expéditeur du courrier électronique](../Response_Actions/RA_1204_get_ability_to_block_email_sender.md)</li><li>[RA1205: Obtenir la possibilité de supprimer un e-mail](../Response_Actions/RA_1205_get_ability_to_delete_email_message.md)</li><li>[RA1206: Obtenir la possibilité de mettre un e-mail en quarantaine](../Response_Actions/RA_1206_get_ability_to_quarantine_email_message.md)</li></ul>|
| **Identification**  |<ul><li>[RA2003: Mettre des comptes compromis sous surveillance](../Response_Actions/RA_2003_put_compromised_accounts_on_monitoring.md)</li><li>[RA2113: Lister les hôtes qui ont communiqués avec un domaine externe](../Response_Actions/RA_2113_list_hosts_communicated_with_external_domain.md)</li><li>[RA2114: Lister les hôtes qui ont communiqués avec une IP externe](../Response_Actions/RA_2114_list_hosts_communicated_with_external_ip.md)</li><li>[RA2115: Lister les hôtes qui ont communiqués avec une URL externe](../Response_Actions/RA_2115_list_hosts_communicated_with_external_url.md)</li><li>[RA2201: Lister les utilisateurs qui ont ouverts un e-mail](../Response_Actions/RA_2201_list_users_opened_email_message.md)</li><li>[RA2202: Collecter l'e-mail](../Response_Actions/RA_2202_collect_email_message.md)</li><li>[RA2203: Lister les destinataires d'un e-mails](../Response_Actions/RA_2203_list_email_message_receivers.md)</li><li>[RA2204: Assurez-vous que le message électronique est du phishing](../Response_Actions/RA_2204_make_sure_email_message_is_phishing.md)</li><li>[RA2205: Extraire les observables du message électronique](../Response_Actions/RA_2205_extract_observables_from_email_message.md)</li></ul>|
| **Containment**  |<ul><li>[RA3101: Bloquer l'adresse IP externe](../Response_Actions/RA_3101_block_external_ip_address.md)</li><li>[RA3103: Bloquer le domaine externe](../Response_Actions/RA_3103_block_external_domain.md)</li><li>[RA3105: Bloquer l'url externe](../Response_Actions/RA_3105_block_external_url.md)</li><li>[RA3201: Bloquer le domaine de l'e-mail](../Response_Actions/RA_3201_block_domain_on_email.md)</li><li>[RA3202: Bloquer l'expéditeur de l'e-mail](../Response_Actions/RA_3202_block_sender_on_email.md)</li><li>[RA3203: Mettre l'e-mail en quarantaine](../Response_Actions/RA_3203_quarantine_email_message.md)</li></ul>|
| **Eradication**  |<ul><li>[RA4001: Signaler l'incident aux sociétés externes](../Response_Actions/RA_4001_report_incident_to_external_companies.md)</li><li>[RA4201: Supprimer l'e-mail](../Response_Actions/RA_4201_delete_email_message.md)</li></ul>|
| **Recovery**  |<ul><li>[RA5101: Débloquer l'ip bloquée](../Response_Actions/RA_5101_unblock_blocked_ip.md)</li><li>[RA5102: Débloquer le domaine bloqué](../Response_Actions/RA_5102_unblock_blocked_domain.md)</li><li>[RA5103: Débloquer l'url bloquée](../Response_Actions/RA_5103_unblock_blocked_url.md)</li><li>[RA5201: Débloquer le domaine de l'e-mail](../Response_Actions/RA_5201_unblock_domain_on_email.md)</li><li>[RA5202: Débloquer l'expéditeur de l'e-mail](../Response_Actions/RA_5202_unblock_sender_on_email.md)</li><li>[RA5203: Restaurer un e-mail en quarantaine](../Response_Actions/RA_5203_restore_quarantined_email_message.md)</li></ul>|
| **Lessons learned**  |<ul><li>[RA6001: Élaborer un rapport d'incident](../Response_Actions/RA_6001_develop_incident_report.md)</li><li>[RA6002: Effectuer un exercice sur les leçons apprises](../Response_Actions/RA_6002_conduct_lessons_learned_exercise.md)</li></ul>|

### Workflow
 
1. Exécutez les actions de réponse étape par étape. Certains d'entre eux sont directement connectés, ce qui signifie que vous ne pourrez pas avancer sans terminer l'étape précédente. Certains d'entre eux sont redondants, comme ceux qui sont liés au blocage d'une menace à l'aide de systèmes de filtrage réseau (étape de confinement)
2. Commencez à exécuter les étapes de confinement et d'éradication simultanément avec les prochaines étapes d'identification, dès que vous recevrez des informations sur les hôtes malveillants
3. Si l'hameçonnage a conduit à l'exécution de code ou à l'accès à distance à l'hôte victime, commencez immédiatement à exécuter le Playbook de réponse aux incidents de post-exploitation générique
4. Enregistrez tous les horodatages des actions mises en œuvre dans le projet de rapport d'incident à la volée, cela vous fera gagner beaucoup de temps



#### Preparation

##### Pratiquez dans l'environnement réel. Affiner les actions de réponse au sein de votre organisation

Assurez-vous que la plupart des actions de réponse ont été effectuées lors d'un exercice interne par votre équipe de réponse aux incidents.
Vous devez vous assurer que lorsqu'un incident se produira, l'équipe n'essaiera pas seulement de suivre les manuels qu'elle voit pour la première fois de sa vie, mais sera en mesure d'exécuter rapidement les étapes réelles dans **votre environnement**, c'est-à-dire le blocage une adresse IP ou un nom de domaine.

##### Suivez des cours de formation pour acquérir des connaissances pertinentes

Voici quelques cours de formation pertinents qui vous aideront dans les activités de réponse aux incidents :  

1. [Investigation Theory](https://chrissanders.org/training/investigationtheory/) par Chris Sanders. Nous vous recommandons de l'avoir comme une formation obligatoire pour chaque membre de votre équipe de réponse aux incidents  
2. Formations [Offensive Security](https://www.offensive-security.com/courses-and-certifications/). Nous recommandons [PWK](https://www.offensive-security.com/pwk-oscp/) pour commencer  
3. Formations [SANS Digital Forensics & Incident Response](https://digital-forensics.sans.org/training/courses)   

Les formations Offensive Security sont dans la liste car pour combattre une menace, vous devez comprendre leur motivation, leurs tactiques et leurs techniques.. 

Dans le même temps, nous supposons que vous avez déjà une solide expérience technique dans les disciplines fondamentales - Réseaux, Systèmes d'exploitation et Programmation.  

##### Assurez-vous que le personnel signalera une activité suspecte, c'est-à-dire des e-mails suspects, des liens, des fichiers, des activités sur leurs ordinateurs, etc.


Développez un moyen simplifié et bien connu de l'entreprise de contacter l'équipe de réponse à incident en cas d'activité suspecte sur le système utilisateur.  
Assurez-vous que le personnel en est conscient, qu'il peut et qu'il l'utilisera.  

##### Raise personnel awareness regarding phishing, ransomware, social engineering,  and other attacks that involve user interaction


Train users to to be aware of access or manipulation attempts by an adversary to reduce the risk of 
successful spearphishing, social engineering, and other techniques that involve user interaction.

##### Assurez-vous d'avoir accès aux journaux de flux réseau de communication externe


Assurez-vous qu'il existe une collection de journaux de flux réseau pour la communication externe (des actifs de l'entreprise à Internet) configurée.  
S'il n'y a pas d'option pour le configurer sur un périphérique réseau, vous pouvez installer un logiciel spécial sur chaque point de terminaison et le collecter à partir d'eux.  

Attention :  

- Il existe une fonctionnalité appelée ["NetFlow Sampling"](https://www.plixer.com/blog/how-accurate-is-sampled-netflow/), cela élimine la valeur des journaux de flux réseau pour certaines des tâches, telles que «vérifier si un hôte a communiqué avec une adresse IP externe». Assurez-vous qu'il est désactivé ou que vous avez un autre moyen de collecter les journaux de flux réseau.  

##### Assurez-vous d'avoir accès aux journaux de communication Web externe (HTTP)


Assurez-vous qu'il existe une collection de journaux de connexions HTTP pour la communication externe (des actifs de l'entreprise à Internet) configurée.  

##### Make sure you have access to external communication DNS logs


Make sure that there is a collection of DNS logs for external communication (from corporate assets to the Internet) configured.  
If there is no option to configure it on a network device/DNS Server, you can install a special software on each endpoint and collect it from them.  

Warning:  

- Make sure that there are both DNS query and answer logs collected. It's quite hard to configure such a collection on MS Windows DNS server and ISC BIND. Sometimes it much easier to use 3rd party solutions to fulfill this requirement.  
- Make sure that DNS traffic to the external (public) DNS servers is blocked by the Border Firewall. This way, corporate DNS servers is the only place assets can resolve the domain names.  

##### Make sure you have the ability to block an external IP address from being accessed by corporate assets


Make sure you have the ability to create a policy rule in one of the listed Mitigation Systems that will you to block an external IP address from being accessed by corporate assets.  

Warning:  

- Make sure that using the listed systems (1 or multiple) you can control access to the internet of all assets in the infrastructure. In some cases, you will need a guaranteed way to block an external IP address from being accessed by corporate assets completely. If some of the assets are not under the management of the listed Mitigation Systems, (so they can access the internet bypassing these systems), you will not be able to fully achieve the final objective of the Response Action.  

##### Make sure you have the ability to block an external domain name from being accessed by corporate assets


Make sure you have the ability to create a policy rule or a specific configuration in one of the listed Mitigation Systems that will you to block an external domain name from being accessed by corporate assets.  

Warning:  

- Make sure that using the listed systems (1 or multiple) you can control access to the internet of all assets in the infrastructure. In some cases, you will need a guaranteed way to block an external domain name from being accessed by corporate assets completely. If some of the assets are not under the management of the listed Mitigation Systems, (so they can access the internet bypassing these systems), you will not be able to fully achieve the final objective of the Response Action.  

##### Make sure you have the ability to block an external URL from being accessed by corporate assets


Make sure you have the ability to create a policy rule or a specific configuration in one of the listed Mitigation Systems that will you to block an external URL from being accessed by corporate assets.  

Warning:  

- Make sure that using the listed systems (1 or multiple) you can control access to the internet of all assets in the infrastructure. In some cases, you will need a guaranteed way to block an external URL from being accessed by corporate assets completely. If some of the assets are not under the management of the listed Mitigation Systems, (so they can access the internet bypassing these systems), you will not be able to fully achieve the final objective of the Response Action.  

##### Make sure you have the ability to list users who opened a particular email message


Make sure you have the ability to list users who opened/read a particular email message using the Email Server's functionality.

##### Make sure you have the ability to list receivers of a particular email message


Make sure you have the ability to list receivers of a particular email message using the Email Server's functionality.

##### Make sure you have the ability to block an email domain


Make sure you have the ability to block an email domain on an Email Server using its native filtering functionality.  

##### Make sure you have the ability to block an email sender


Make sure you have the ability to block an email sender on an Email Server using its native filtering functionality.  

##### Make sure you have the ability to delete an email message


Make sure you have the ability to delete an email message from an Email Server and users' email boxes using its native functionality.

##### Make sure you have the ability to quarantine an email message


Make sure you have the ability to quarantine an email message on an Email Server using its native functionality.  

#### Identification

##### Put (potentially) compromised accounts on monitoring

Start monitoring for authentification attempts and all potentially harmful actions from (potentially) compromised accounts.  
Look for anomalies, unusual network connections, unusual geolocation/time of work, actions that were never executed before.  
Keep in touch with the real users and, in case of need, ask them if they executing some suspicious actions by themselves or not.  

##### List hosts communicated with an external domain


List hosts communicated with an external domain using the most efficient way.  

##### List hosts communicated with an external IP address


List hosts communicated with an external IP address using the most efficient way.  

##### List hosts communicated with an external URL


List hosts communicated with an external URL using the most efficient way.  

##### List users that have opened am email message


List users who opened/read a particular email message using the Email Server's functionality.  

##### Collect an email message

Collect an email message using the most appropriate option:  

- Email Team/Email server: if there is such option  
- The person that reported the attack (if it wasn't detected automatically or reported by victims)  
- Victims: if they reported the attack  
- Following the local computer forensic evidence collection procedure, if the situation requires it

Ask for the email in `.EML` format. Instructions:  

  1. Drug and drop email from Email client to Desktop  
  2. Archive with password "infected" and send to IR specialists by email  

##### List receivers of a particular email message


List receivers of a particular email message using the Email Server's functionality.  

##### Make sure that an email message is a phishing attack

Check an email and its metadata for evidences of phishing attack:  

- **Impersonalisation attempts**: sender is trying to identify himself as somebody he is not  
- **Suspicious askings or offers**: download "invoice", click on link with something important etc  
- **Psychological manipulations**: invoking a sense of urgency or fear is a common phishing tactic  
- **Spelling mistakes**: legitimate messages usually don't have spelling mistakes or poor grammar  

Explore references of the article to make yourself familiar with phishing attacks history and examples.  

##### Extract observables from an email message

Extract the data for further response steps:  

- attachments (using munpack tool: `munpack email.eml`)  
- from, to, cc  
- subject of the email  
- received servers path  
- list of URLs from the text content of the mail body and attachments  

This Response Action could be automated with [TheHive EmlParser](https://blog.thehive-project.org/2018/07/31/emlparser-a-new-cortex-analyzer-for-eml-files/).  

#### Containment

##### Block an external IP address from being accessed by corporate assets


Block an external IP address from being accessed by corporate assets, using the most efficient way.  

Warning:  

- Be careful blocking IP addresses. Make sure it's not a cloud provider or a hoster. If you would like to block something that is hosted on a well-known cloud provider or on a big hoster IP address, you should block (if applicable) a specific URL using alternative Response Action   

##### Block an external domain name from being accessed by corporate assets


Block an external domain name from being accessed by corporate assets, using the most efficient way.  

Warning:  

- Be careful blocking doman names. Make sure it's not a cloud provider or a hoster. If you would like to block something that is hosted on a well-known cloud provider or on a big hoster doman, you should block (if applicable) a specific URL using alternative Response Action   

##### Block an external URL from being accessed by corporate assets


Block an external URL from being accessed by corporate assets, using the most efficient way.  

##### Block a domain name on an Email server

Block a domain name on an Email Server using its native filtering functionality.  

##### Block an email sender on the Email-server


Block an email sender on an Email Server using its native filtering functionality.  

##### Quarantine an email message


Quarantine an email message on an Email Server using its native functionality.  

#### Eradication

##### Report incident to external companies

Report incident to external security companites, i.e. [National Computer Security Incident Response Teams (CSIRTs)](https://www.sei.cmu.edu/education-outreach/computer-security-incident-response-teams/national-csirts/).  
Provide all Indicators of Compromise and Indicators of Attack that have been observed.  

A phishing attack could be reported to:  

1. [National Computer Security Incident Response Teams (CSIRTs)](https://www.sei.cmu.edu/education-outreach/computer-security-incident-response-teams/national-csirts/)  
2. [U.S. government-operated website](http://www.us-cert.gov/nav/report_phishing.html)  
3. [Anti-Phishing Working Group (APWG)](http://antiphishing.org/report-phishing/)  
4. [Google Safe Browsing](https://safebrowsing.google.com/safebrowsing/report_phish/?hl=en)  
5. [The FBI's Intenet Crime Complaint Center (IC3)](https://www.ic3.gov/default.aspx)  

This Response Action could be automated with [TheHive and MISP integration](https://blog.thehive-project.org/2017/06/19/thehive-cortex-and-misp-how-they-all-fit-together/).  

##### Delete an email message from an Email Server and users' email boxes

Delete an email message from an Email Server and users' email boxes using its native functionality.

#### Recovery

##### Unblock a blocked IP address


Unblock a blocked IP address in the system(s) used to block it.  

##### Unblock a blocked domain name


Unblock a blocked domain name in the system(s) used to block it.  

##### Unblock a blocked URL


Unblock a blocked URL in the system(s) used to block it.  

##### Unblock a domain on email


Unblock an email domain on an Email Server using its native functionality.  

##### Unblock a sender on email


Unblock an email sender on an Email Server using its native functionality.  

##### Restore a quarantined email message


Restore a quarantined email message on an Email Server using its native functionality.  

#### Lessons learned

##### Develop the incident report

Develop the Incident Report using your corporate template.  

It should include:  

1. Executive Summary with a short description of damage, actions taken, root cause, and key metrics (Time To Detect, Time To Respond, Time To Recover etc)  
2. Detailed timeline of adversary actions mapped to [ATT&CK tactics](https://attack.mitre.org/tactics/enterprise/) (you can use the [Kill Chain](https://en.wikipedia.org/wiki/Kill_chain), but most probably most of the actions will be in Actions On Objective stage, which is not very representative and useful)  
3. Detailed timeline of actions taken by Incident Response Team  
4. Root Cause Analysis and Recommendations for improvements based on its conclusion  
5. List of specialists involved in Incident Response with their roles  

##### Conduct Lessons Learned exercise

The Lessons Learned phase evaluates the team's performance through each step. 
The goal of the phase is to discover how to improve the incident response process.  
You need to answer some basic questions, using developed incident report:  

- What happened?  
- What did we do well?  
- What could we have done better?  
- What will we do differently next time?  

The incident report is the key to improvements.  














