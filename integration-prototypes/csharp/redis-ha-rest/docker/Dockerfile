FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY src/RedisHaRestService/RedisHaRestService.csproj src/RedisHaRestService/
RUN dotnet restore src/RedisHaRestService/RedisHaRestService.csproj
COPY src/RedisHaRestService/ src/RedisHaRestService/
RUN dotnet publish src/RedisHaRestService/RedisHaRestService.csproj -c Release -o /app/publish /p:UseAppHost=false
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/publish ./
ENV ASPNETCORE_URLS=http://+:8080
EXPOSE 8080
ENTRYPOINT ["dotnet", "RedisHaRestService.dll"]
