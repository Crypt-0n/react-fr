| Titre                       | Accéder aux journaux HTTP externes         |
|:---------------------------:|:--------------------|
| **ID**                      | RA1104            |
| **Description**             | Assurez-vous d'avoir accès aux journaux de communication Web externe (HTTP)   |
| **Auteur**                  | @atc_project        |
| **Creation Date**           | 06.05.2020 |
| **Catégorie**                | Network      |
| **Étapes**                   |[RS0001: Préparation](../Response_Stages/RS0001.md)| 
| **References** |<ul><li>[https://docs.zeek.org/en/current/examples/httpmonitor/](https://docs.zeek.org/en/current/examples/httpmonitor/)</li><li>[https://en.wikipedia.org/wiki/Common_Log_Format](https://en.wikipedia.org/wiki/Common_Log_Format)</li></ul>|
| **Requirements** |<ul><li>MS_border_proxy</li><li>MS_border_ngfw</li><li>DN_zeek_http_log</li></ul>|

### Workflow

Assurez-vous qu'il existe une collection de journaux de connexions HTTP pour la communication externe (des actifs de l'entreprise à Internet) configurée.  
