| Title                       | Accéder aux journaux des flux réseaux externes   |
|:---------------------------:|:--------------------|
| **ID**                      | RA1101            |
| **Description**             | Assurez-vous d'avoir accès aux journaux de flux réseau de communication externes   |
| **Author**                  | @atc_project - Traduit et Mise à jour par Crypt-0n       |
| **Creation Date**           | 11.06.2020 |
| **Category**                | Réseau      |
| **Stage**                   |[RS0001: Preparation](../Response_Stages/RS0001.md)| 
| **References** |<ul><li>[https://fr.wikipedia.org/wiki/NetFlow](https://fr.wikipedia.org/wiki/NetFlow)</li><li>[https://www.plixer.com/blog/how-accurate-is-sampled-netflow/](https://www.plixer.com/blog/how-accurate-is-sampled-netflow/)</li></ul>|
| **Requirements** |<ul><li>MS_border_firewall</li><li>MS_border_ngfw</li><li>DN_zeek_conn_log</li></ul>|

### Workflow

Assurez-vous qu'il existe une collecte de journaux de flux réseau pour la communication externe (des actifs de l'entreprise à Internet) configurée.
S'il n'y a pas d'option pour la configurer sur un périphérique réseau, vous pouvez installer un logiciel spécial sur chaque point de terminaison et la collecter à partir d'eux. 

Warning:  
Il existe une fonctionnalité appelée ["NetFlow Sampling"](https://www.plixer.com/blog/how-accurate-is-sampled-netflow/) , qui élimine la valeur des journaux de flux réseau pour certaines des tâches, tel que "vérifier si un hôte a communiqué avec une adresse IP externe". Assurez-vous qu'il est désactivé ou que vous avez un autre moyen de collecter les journaux de flux réseau
