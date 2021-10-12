### [965. Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/)

Easy

Every __valid email__ consists of a __local name__ and a __domain name__, separated by the `` '@' `` sign. Besides lowercase letters, the email may contain one or more `` '.' `` or `` '+' ``.

*   For example, in `` "alice@leetcode.com" ``, `` "alice" `` is the __local name__, and `` "leetcode.com" `` is the __domain name__.

If you add periods `` '.' `` between some characters in the __local name__ part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule __does not apply__ to __domain names__.

*   For example, `` "alice.z@leetcode.com" `` and `` "alicez@leetcode.com" `` forward to the same email address.

If you add a plus `` '+' `` in the __local name__, everything after the first plus sign __will be ignored__. This allows certain emails to be filtered. Note that this rule __does not apply__ to __domain names__.

*   For example, `` "m.y+name@email.com" `` will be forwarded to `` "my@email.com" ``.

It is possible to use both of these rules at the same time.

Given an array of strings `` emails `` where we send one email to each `` email[i] ``, return _the number of different addresses that actually receive mails_.

 

__Example 1:__

```
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
```

__Example 2:__

```
Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
```

 

__Constraints:__

*   `` 1 <= emails.length <= 100 ``
*   `` 1 <= emails[i].length <= 100 ``
*   `` email[i] `` consist of lowercase English letters, `` '+' ``, `` '.' `` and `` '@' ``.
*   Each `` emails[i] `` contains exactly one `` '@' `` character.
*   All local and domain names are non-empty.
*   Local names do not start with a `` '+' `` character.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 458,062 | 309,050 | 67.5% |